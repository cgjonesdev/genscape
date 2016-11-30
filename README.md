# Genscape

<center><h2>Bowling Scoring API</h2></center>

> An API to score the game of bowling.

### Setup
1. [Create and activate a python virtualenv](http://virtualenvwrapper.readthedocs.io/en/latest/install.html).
1. [Install Django Rest Framework](http://www.django-rest-framework.org/#installation).
1. Clone the bowling project: `git@github.com:cgjonesdev/genscape.git`.
1. Prep the database:
	1. `python manage.py makemigrations scoring`
	1. `python manage.py migrate`
1. Start the development web server
	1. `python manage.py runserver`

### Create a Player
1. Navigate to the `/players` endpoint of the api
	1. In a browser, enter `localhost:8000/players`.
	1. Enter only the name of a player and click the `POST` button.

> The other parameters can be set, but will affect the game. These were set to read-only in the serializers module initially, but prevented the user from viewing the score as they bowl, so they were set back to editable.

### Start Bowling
1. Navigate to the `/players/1/bowl` endpoint.
> The player will have thrown their first roll. You can see the score for the first roll for frame #1. Number of knocked pins for each roll is random unless a query string is used.

1. To continue bowling, hit refresh on the browser and watch the score tally up and the frames advance.

#### To Set the Number of Knocked Down Pins
> To see how the API handles scoring for strikes and spares (instead of waiting for them to randomly come up), add a querystring

##### Examples:
* Strike:
	* First roll: `/players/1/bowl/?first_roll=10`
* Spare:
	* First and second roll: `/players/1/bowl/?first_roll=7&second_roll=3`
* First roll only: `/players/1/bowl/?first_roll=7`
* Second roll only: `/players/1/bowl/?second_roll=5`

### Stats
> Each players all-time-score and number of games bowled is recorded
