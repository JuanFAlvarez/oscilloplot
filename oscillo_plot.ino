const byte FIGURE_DELAY = 1; // trace delay in uS. adjust if needed
const int NUM_POINTS = 87;// number of XY points in figure

// x and y coordinates to plot 
byte x_points[NUM_POINTS] = {106,106,105,104,103,102,101,100,99,98,97,96,95,94,93,92,91,90,90,89,88,87,87,87,86,86,86,86,87,89,90,91,93,95,97,99,101,102,102,104,104,105,105,106,106,106,106,106,106,108,109,110,112,113,115,117,119,121,122,123,123,124,124,124,124,124,123,122,121,120,119,118,117,116,115,114,113,112,111,110,110,109,109,109,108,107,107};
byte y_points[NUM_POINTS] = {78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,99,100,101,103,105,106,108,110,112,113,113,114,115,115,115,115,115,115,114,112,112,110,109,107,106,106,108,110,112,114,114,115,116,116,117,117,117,117,117,116,115,113,112,110,108,106,104,103,102,100,99,98,97,96,95,94,93,92,91,90,89,87,86,84,82,81,80,78};


void setup(){
  // initialize port D and B for writing
  DDRD = B11111111; 
  DDRB = B00111111;
  byte t;
  for (t=0; t < NUM_POINTS; t++)
  {
    y_points[t] = map(y_points[t],0,255,0,63); // re-map Y points to 6 bits since port B is limited to 6 bits on Arduino
  }
}

void loop(){
    for (byte t=0; t < NUM_POINTS; t++)// run through points
    { 
      PORTD = x_points[t];
      PORTB = y_points[t];
      delayMicroseconds(FIGURE_DELAY);
    }
}

  
  
  
