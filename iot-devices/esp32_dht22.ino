#include <WiFi.h>
#include <HTTPClient.h>
#include <DHT.h>

#define DHTPIN 4
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);

const char* ssid = "YOUR_WIFI_SSID";
const char* password = "YOUR_WIFI_PASSWORD";
const char* serverUrl = "http://api-gateway-ip/api/android/sensor-data";

void setup() {
  Serial.begin(115200);
  dht.begin();
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
  }
}

void loop() {
  float temp = dht.readTemperature();
  float hum = dht.readHumidity();

  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(serverUrl);
    http.addHeader("Content-Type", "application/json");

    String jsonPayload = "{\"truck_id\":\"TRK-001\",\"current_temperature\":" + String(temp) + ",\"humidity\":" + String(hum) + "}";
    int httpResponseCode = http.POST(jsonPayload);
    
    http.end();
  }
  delay(10000); // Kirim setiap 10 detik
}
