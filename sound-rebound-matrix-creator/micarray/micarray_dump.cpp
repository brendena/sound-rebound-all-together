/*
 * Copyright 2016 <Admobilize>
 * All rights reserved.
 */

#include <wiringPi.h>

#include <string>
#include <fstream>
#include <iostream>
#include <valarray>

#include <matrix_hal/everloop_image.h>
#include <matrix_hal/everloop.h>
#include <matrix_hal/microphone_array.h>
#include <matrix_hal/wishbone_bus.h>

namespace hal = matrix_hal;

int main(int argc, char *argv[]) {
  hal::WishboneBus bus;
  bus.SpiInit();

  hal::MicrophoneArray mics;
  mics.Setup(&bus);

  hal::Everloop everloop;
  everloop.Setup(&bus);

  hal::EverloopImage image1d;

  char * pEnd;
  long red = 0;
  long blue = 0;
  long green = 0;
  long seconds_to_record = 1;
  long fileItteration = 0;

  if(argc == 6){
    fileItteration = strtol(argv[1],&pEnd,10);
    seconds_to_record = strtol(argv[2],&pEnd,10);
    red = strtol(argv[3],&pEnd,10);
    blue = strtol(argv[4], &pEnd,10);
    green = strtol(argv[5], &pEnd, 10);
  }

  for (auto& led : image1d.leds) {
    led.blue = blue;
    led.red = red;
    led.green = green;
  }
  everloop.Write(&image1d);


  int16_t buffer[mics.Channels() + 1][seconds_to_record * mics.SamplingRate()];

  mics.CalculateDelays(0, 0, 1000, 320 * 1000);
  /*////////////////////////////////////////////
  / About setGain
  / http://community.matrix.one/t/low-energy-on-array-microphones/281/8
  /
  / https://github.com/matrix-io/matrix-creator-hal/blob/master/cpp/driver/microphone_array.h#L41
  ////////////////////////////////////////////*/
  mics.SetGain((int16_t) 8);
  uint32_t step = 0;
  while (true) {
    mics.Read(); /* Reading 8-mics buffer from de FPGA */

    for (uint32_t s = 0; s < mics.NumberOfSamples(); s++) {
      for (uint16_t c = 0; c < mics.Channels(); c++) { /* mics.Channels()=8 */
        buffer[c][step] = mics.At(s, c);
      }
      buffer[mics.Channels()][step] = mics.Beam(s);
      step++;
    }
    if (step == seconds_to_record * mics.SamplingRate()) break;
  }


  std::string filename = "mic_" + std::to_string(fileItteration) + ".raw";
  std::ofstream os(filename, std::ofstream::binary);
  os.write((const char*)buffer[0],
           seconds_to_record * mics.SamplingRate() * sizeof(int16_t));

  os.close();
  std::cout << filename;
  std::cout.flush();


  return 0;
}