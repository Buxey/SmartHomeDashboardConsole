# SmartHome Dashboard Console

This is a Smart Home Dashboard Console that we had been given as coursework for our programming module using Java, but upon finding Java & OOP extremely difficult (just barely getting my pass), I decided to redo the coursework again during the summer to make sure to the best of my ability I understood OOP principles.

The basic premise of this project is to use OOP principles to manage as many or as few Rooms & Smart plugs as we wanted and to further manipulate the smart plugs that would be stored/built in the backend of our project. 


The Dashboard is our client that would take all the information from the user and then pass that up the stream to the correct class keeping everything separate and only being able to talk to one other class which was the SmartHome Class. 


The Smarthome Class is where we keep all of our methods to manipulate the Rooms as we like whether that be building the rooms getting their information and so on we have achieved this by using getters and setters.

The Room Class which connects to the SmartHome Class this is where the Rooms are built and stored, once again allowing us to call certain methods to achieve the tasks we have been given, this class is the only class that will talk to our final class the SmartPlug Class.

Finally, the final class we have is the SmartPlug class. This class puts everything together and gives us for example (SmartPlug | Attached To: Phone Recharger | Room: Bedroom | SmartPlug ID: 1 | Status: False) this class accepts all the information that has been pushed up through the stream and is only used using our getters and setters as we please and displaying all the information in regards to our Room and Smart Plug

Overall I learned a lot from this project and have obtained a little bit better understanding of how to use OOP principles and why they are so beneficial and used extensively in the working world.
