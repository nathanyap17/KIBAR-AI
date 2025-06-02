#include <Arduino.h>

// Function prototypes
void displayBraille(int index);
void clearBraille();

// Braille patterns
int braille[26][6] = {
  {1,0,0,0,0,0}, {1,0,1,0,0,0}, {1,1,0,0,0,0}, {1,1,0,1,0,0},
  {1,0,0,1,0,0}, {1,1,1,0,0,0}, {1,1,1,1,0,0}, {1,0,1,1,0,0},
  {0,1,1,0,0,0}, {0,1,1,1,0,0}, {1,0,0,0,1,0}, {1,0,1,0,1,0},
  {1,1,0,0,1,0}, {1,1,0,1,1,0}, {1,0,0,1,1,0}, {1,1,1,0,1,0},
  {1,1,1,1,1,0}, {1,0,1,1,1,0}, {0,1,1,0,1,0}, {0,1,1,1,1,0},
  {1,0,0,0,1,1}, {1,0,1,0,1,1}, {0,1,1,1,0,1}, {1,1,0,0,1,1},
  {1,1,0,1,1,1}, {1,0,0,1,1,1}
};

// Control pins
int controlPins[6] = {7, 6, 5, 4, 3, 2};

void setup() {
  Serial.begin(115200);
  for (int i = 0; i < 6; i++) {
    pinMode(controlPins[i], OUTPUT);
  }
}

void loop() {
  if (Serial.available()) {
    char receivedChar = Serial.read(); // Read one character
    
    int index = -1; // Initialize index to an invalid value

    if (receivedChar >= 'A' && receivedChar <= 'Z') { 
      // Uppercase letter
      index = receivedChar - 'A'; // Convert uppercase letter to index
    } 
    else if (receivedChar >= 'a' && receivedChar <= 'z') {
      // Lowercase letter
      index = receivedChar - 'a'; // Convert lowercase letter to index
    }

    // Display Braille pattern if the letter is valid
    if (index >= 0 && index < 26) {
      clearBraille();            // Clear before displaying
      displayBraille(index);     // Display new pattern
      delay(1000);               // Hold the pattern for 1 second
      clearBraille();            // Clear after holding
    }

    // Clear any memory before proceed with the following letters
    Serial.flush();

  }
}

// Function definitions
void displayBraille(int index) {
  for (int k = 0; k < 6; k++) {
    digitalWrite(controlPins[k], braille[index][k]); // Trigger all actuators simultaneously
  }
}

void clearBraille() {
  for (int k = 0; k < 6; k++) {
    digitalWrite(controlPins[k], LOW); // Turn off all actuators
  }
}

