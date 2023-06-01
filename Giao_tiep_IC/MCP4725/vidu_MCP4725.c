#include "16f877a.h"
#use delay(clock=16M)
#use i2c(master,sda=PIN_C4, scl=PIN_C3, FAST=100000) 
#use rs232(baud=9600,xmit=pin_C6,rcv=pin_C7) 
void R_mcp4725();
void W_mcp4725();
void main(){
   W_mcp4725();
   while(1){
      R_mcp4725();
      delay_ms(1000);
   }
}
void R_mcp4725(){
   i2c_start();
   i2c_write(193);
   unsigned int data1 = i2c_read(1);
   if(data1 >127)
      for(int i=0;i<4;i++){
         data1 = i2c_read(1);
         printf("byte=%u \n\r",data1);
      }
   i2c_stop();
}

void W_mcp4725(){
   i2c_start();
   i2c_write(192);
   i2c_write(96);
   i2c_write(125);
   i2c_write(0);
   i2c_stop();
}
