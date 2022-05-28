# IOT-Lab-6

# Lab 6

## Aim

This lab is meant to get students more accustomed to the technologies used in designing and implementing a WiFi enabled embedded dev module as part of an IoT system and RESTful API server.

## Requirements

### Client

For the final part of the system you're meant to build, you'll have to send status updates from each deployed tank. Your goal is to design a circuit based on an Espressif based development module (eg. ESP8266, ESP32, etc.).

Your embedded system should continuously send POST requests to your server from the embedded circuit. 

Your POST request should send a JSON object as payload.

Your JSON body should formatted as follows:

```json
{
	"tank_id": <id>, 
	"water_level": <water level>
} 
```

Since we currently don't all have the hardware required to measure the volume or height of water or water level in the tank, we'll have to simulate the response using other hardware if necessary. 

In your arduino sketch, include a function called `getWaterLevel`. This function should return an integer value read from a sensor of your choosing. This function should be used to read the value from an ultrasonic sensor, ideally, or if one is not available, a digital/analog temperature sensor or any other hardware component capable of outputting a varying signal readable by the ESP dev module.

This function should be used to populate the `water_level` attribute of your request's JSON body. 

With this design, you'll have to programmatically construct the JSON body using an appropriate JSON library.

The `tank_id` attribute of the JSON body should be populated with the MAC address of the dev module. This can be pulled programmatically and saved locally in your adruino sketch.

### Server

You'll have to add a new route handler to your API. The route handler function should accept a POST request on the path "/tank": `POST /tank`.

The response of this API call should be a JSON with a suitable success message, the time of the response and a boolean value that should be set to `true` if the posted `water_level` was between 80 and 100, inclusively, and `false` otherwise, eg:

```json
{
	"led": true,
	"msg": "data saved in database successfully",
	"date": "<datetime of respsonse>",
}
```

### Embedded Design

The `led` attribute in the JSON response should be used to control the state of an LED connected to your ESP32. If `led` is `true`, the led should light. The led should be off otherwise.

### Database

You'll also need to add a new marshmallow schema to your application. This would also mean that a new collection will be added to the database that you're application communicates with.  The schema should be called `Level` and a level should consist of a `tank_id` and a `percentage_full`. These two values should be written to the `levels` collection.
