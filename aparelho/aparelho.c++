#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <SD.h>
#include <SPI.h>
#include <TMRpcm.h>

#define OLED_RESET    -1
#define SCREEN_WIDTH  128
#define SCREEN_HEIGHT 64
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

#define SD_CS   10
#define AUDIO_PIN 9

#define BTN_NEXT 2
#define BTN_PREV 3
#define BTN_PLAY 4
#define BTN_STOP 5

TMRpcm audio;
File root;
String songs[10];
int songCount = 0;
int currentSong = 0;
bool isPlaying = false;

void setup() {
    pinMode(BTN_NEXT, INPUT_PULLUP);
    pinMode(BTN_PREV, INPUT_PULLUP);
    pinMode(BTN_PLAY, INPUT_PULLUP);
    pinMode(BTN_STOP, INPUT_PULLUP);
    
    Serial.begin(9600);
    
    if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
        Serial.println(F("Display OLED não encontrado!"));
        while (1);
    }
    display.clearDisplay();
    display.setTextSize(1);
    display.setTextColor(WHITE);
    display.setCursor(0, 0);
    display.println("Iniciando...");
    display.display();
    
    if (!SD.begin(SD_CS)) {
        Serial.println("Falha ao inicializar o SD!");
        while (1);
    }
    
    audio.speakerPin = AUDIO_PIN;
    carregarMusicas();
    atualizarDisplay();
}

void loop() {
    if (digitalRead(BTN_NEXT) == LOW) {
        proximaMusica();
    }
    if (digitalRead(BTN_PREV) == LOW) {
        musicaAnterior();
    }
    if (digitalRead(BTN_PLAY) == LOW) {
        tocarMusica();
    }
    if (digitalRead(BTN_STOP) == LOW) {
        pararMusica();
    }
    delay(200);
}

void carregarMusicas() {
    root = SD.open("/");
    songCount = 0;
    while (true) {
        File entry = root.openNextFile();
        if (!entry) break;
        if (String(entry.name()).endsWith(".wav")) {
            songs[songCount] = String(entry.name());
            songCount++;
        }
        entry.close();
    }
}

void atualizarDisplay() {
    display.clearDisplay();
    display.setCursor(0, 0);
    display.println("Tocando:");
    display.println(songs[currentSong]);
    display.display();
}

void tocarMusica() {
    if (!isPlaying) {
        audio.play(songs[currentSong].c_str());
        isPlaying = true;
        atualizarDisplay();
    }
}

void pararMusica() {
    audio.stopPlayback();
    isPlaying = false;
    atualizarDisplay();
}

void proximaMusica() {
    currentSong = (currentSong + 1) % songCount;
    if (isPlaying) tocarMusica();
    atualizarDisplay();
}

void musicaAnterior() {
    currentSong = (currentSong - 1 + songCount) % songCount;
    if (isPlaying) tocarMusica();
    atualizarDisplay();
}
