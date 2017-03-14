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


namespace hal = matrix_hal;

int main() {
  hal::WishboneBus* bus = new hal::WishboneBus();
  bus->SpiInit();

  hal::MicrophoneArray mics;
  mics.Setup(bus);

  pinMode(13, OUTPUT);
  pinMode(5, OUTPUT);

  digitalWrite(13, HIGH);
  digitalWrite(5, HIGH);

  hal::Everloop everloop;
  everloop.Setup(bus);

  hal::EverloopImage image1d;

  for (auto& led : image1d.leds) led.blue = 10;

  everloop.Write(&image1d);

  usleep(9000000);

  for (auto& led : image1d.leds) {
    led.blue = 0;
    led.red = 10;
  }
  everloop.Write(&image1d);
  
  usleep(9000000);

  for (auto& led : image1d.leds) {
    led.red = 0;
    led.green = 10;
  }
  everloop.Write(&image1d);
  
  usleep(9000000);
  
  for (auto& led : image1d.leds){
		led.red = 0;
		led.green = 0;
		led.blue = 0;
		
	}
  everloop.Write(&image1d);
  
  digitalWrite(13, LOW);
  digitalWrite(5, LOW);
  return 0;
}
