/*
 * Copyright 2016 <Admobilize>
 * All rights reserved.
 */
#include <wiringPi.h>

#include <string>
#include <iostream>
#include <valarray>
#include <unistd.h>

#include <matrix_hal/everloop_image.h>
#include <matrix_hal/everloop.h>
#include <matrix_hal/microphone_array.h>
#include <matrix_hal/wishbone_bus.h>
#include <stdlib.h>
#include "./libmfcc/libmfcc.h"



namespace hal = matrix_hal;

int main(int argc, char *argv[]) {
  hal::WishboneBus* bus = new hal::WishboneBus();
  bus->SpiInit();

  hal::MicrophoneArray mics;
  mics.Setup(bus);

/*
  pinMode(13, OUTPUT);
  pinMode(5, OUTPUT);

  digitalWrite(13, HIGH);
  digitalWrite(5, HIGH);
*/
  hal::Everloop everloop;
  everloop.Setup(bus);

  hal::EverloopImage image1d;

  uint16_t seconds_to_record = 1;

  double buffer[mics.Channels()][seconds_to_record * mics.SamplingRate()];

  uint32_t step = 0;

  char * pEnd;
  long red = 0;
  long blue = 0;
  long green = 0;
  if(argc == 4){
	red = strtol(argv[1],&pEnd,10);
	blue = strtol(argv[2], &pEnd,10);
	green = strtol(argv[3], &pEnd, 10);
  }

  for (auto& led : image1d.leds) {
    led.blue = blue;
    led.red = red;
    led.green = green;
  }
  everloop.Write(&image1d);

  while (true) {
    mics.Read(); /* Reading 8-mics buffer from de FPGA */

    for (uint32_t s = 0; s < mics.NumberOfSamples(); s++) {
      for (uint16_t c = 0; c < mics.Channels(); c++) { /* mics.Channels()=8 */
        buffer[c][step] = mics.At(s, c);
      }
      step++;
    }
    if (step == seconds_to_record * mics.SamplingRate()) break;
  }

  uint16_t c = 0;
  ///*
  std::cout.write((const char*)buffer[c],
                  seconds_to_record * mics.SamplingRate() * sizeof(int16_t));
  
  std::cout.flush();
	//*/
  for (auto& led : image1d.leds) {
    led.red = 0;
    led.green = 0;
    led.blue = 0;
  }
  everloop.Write(&image1d);
  
  /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  /   sending data over cout
	/   where python will convert
  /   these strings into list
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/


  /*
  double mfcc_result;
  for(unsigned int coeff = 0; coeff < 13; coeff++){
		mfcc_result = GetCoefficient(buffer[0],44100,48,128, coeff);
		std::printf("%f , ", mfcc_result);
	}
  std::cout.flush();
  */
  

  
	
  
  return 0;
}
