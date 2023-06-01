// IC74HC595 dau tien la 0(Pos0), moi lan qua n IC thi se la N(PosN)
Unsigned int8 CLk,DS,LATCH;
Unsigned int8 IC,mang_data[]={0,0,0,0,0,0,0,0};
void khoitao_74HC595(Unsigned int8 Clock,Unsigned int8 Data,Unsigned int8 Latch_data,Unsigned int8 Num_74HC595){
   CLK=Clock;
   DS=Data;
   LATCH=Latch_data;
   IC=Num_74HC595;
   for(int n=0;n<IC;n++)
      mang_data[n]=0;
}
void set_74HC595(Unsigned int8 Pos,Unsigned int8 Data_set){
   mang_data[IC-1-Pos]=Data_set;
   output_bit(LATCH,0);
   for(int Num_Ic=0;Num_Ic<IC;Num_Ic++){
      for(int i=15;i+1>0;i--){
         output_bit(DS,i%2==1&&bit_test(mang_data[Num_Ic],i/2)?1:0);
         output_bit(CLK,i%2==1?1:0);
      }
   }
   output_bit(LATCH,1);
}

