$(document).ready(function () {
  client = mqtt.connect("wss://test.mosquitto.org:8081/mqtt");
  client.on("connect", function () {
    console.log("Successfully connected");
  })
  client.on("message", function (topic, payload) {
    console.log("recieved:\ntopic: " + topic + "\npayload: " + payload);
  })
  $("#on").click(function(){
    client.publish("x","1");
  
  })
  $("#off").click(function(){
    client.publish("x","0"); 
    
  })

})
