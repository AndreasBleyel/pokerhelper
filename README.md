# pokerhelper

Welcome to the pokerhelper. This Phyton-based application will
help you to evaluate your chances of winning a hand in Texas-HoldEm NoLimit.

### How to run the application:
1. Download or clone the repo onto your PC
2. Get [python3](https://www.python.org/downloads/release/python-372/) for your system 
3. This application uses the [poker-odds-calculator](https://rapidapi.com/sf-api-on-demand/api/poker-odds-calculator?utm_source=mashape&utm_medium=301) API
You need to register and get your own API-Key.
4. Go to the folder where you have downloaded the repo to. Create a 
'ApiValues.py' file with a text editor of your choice and paste the following text: 
`api_key = "ENTER YOUR API KEY HERE"
api_url = "https://sf-api-on-demand-poker-odds-v1.p.mashape.com/"
api_headers = {"X-Mashape-Key": api_key,
                "Accept": "application/json"}`  
5. enter your terminal and start the application with `phyton3 main.py`

### How to use
After the application has started, you will see 5 different areas 
each of them serving a different purpose.

**Board/Hand** 
Here you see the cards which are currently on the board and in your hand. 
You can **add cards** simply by clicking at the desired card down at the
card pool. Notice the red rectangle around one card from the board or hand.
This indicator shows which card will be set, replaced or removed. You can
set the focus on any card simply by clicking on it. By default, the focus
will automatically jump to the next card after setting a card.

**Card Pool**
Display all of the 52 available cards. By clicking on one of them, you will
set the currently focused card with its value. 

**Bids and Pot Size**
To calculate the Pot-Odds, you need to input the current pot size and how much your opponent bids. 
Any positive number > 0 is allowed. For decimals use **.** If it is you to start bidding, leave the
_Bid Opponent_ at 0. In this case, you only get your Chances to hit a specific hand. Pot-Odds calculation
is only possible when both values are entered.

**Calc/Remove Card/Remove All**
After entering at least your hand, you can hit the **Calc** button. Hitting this button will trigger
the API-Call and send your hand and eventually the board to the API. It may take a few seconds to receive the answer. After that, the results will be displayed in the area to the right.

To **remove a card** from your hand or the board, simply select the card and click **Remove Card**. It is
also possible, overwrite the card with another value. For that, select the desired card and click on
the card with the new value. 

If you want to reset all cards (for example when a new round starts) just press the **Remove All* button.

**Display Area**
At the right, you will find the results from the API-Call and the internal calculations. 

On top, you will see your **Chances to hit a specific hand**. Sometimes you will see your chances to hit
a _Straight Flush_ displayed with 0.00% even though it theoretically has a chance (but then it usually is 
smaller than 0.01%.)

The next section shows 3 kinds of hands you could hit and their respective rank. 
Firstly the _Highest possible hand_ followed by the _Average possible hand_ and at least the _Worst possible hand_.
Usually, you will need the _Average possible hand_ for your decision to keep on playing or not.

The last 2 blocks will display a recommendation based on the Pott Ods and your Odds for you _Best_ and _Average_ possible hand.
If your Odds are greater or equal then the Pot Odds you should bet. If they are they smaller you should fold.
When a player holds a drawing hand (a hand that is behind now but is likely to win if a certain card is 
drawn) pot odds are used to determine the expected value of that hand when the player is faced with a bet.
The expected value of a call is determined by comparing the pot odds to the odds of drawing a card that wins the pot. When the odds of drawing a card that wins the pot are numerically higher than the pot odds, 
the call has a positive expectation; on average, a portion of the pot that is greater than the cost of the call is won. Conversely, if the odds of drawing a winning card are numerically lower than the pot odds, 
the call has a negative expectation, and the expectation is to win less money on average than it costs to
call the bet. The Odds are calculated based on your hand and the board. For a deeper explanation of Pots Odds see [Wiki-PotOdds](https://en.wikipedia.org/wiki/Pot_odds)
**Notice:** In the above calculations, the simplistic assumption is that you are sitting behind an opponent. So if you are the first to bid and
enter a Pot-Size of 0, you will always get the recommendation to "call". Even if your chances to hit a specific
card are high, the Odds are to your favor and you get the recommendation to make the call, it does not mean that
you will win this hand. This application only tells you if your bet is reasonable (from a mathematical view)
compared to the Pot-Size and your possibilities to hit a specific hand. Of course, it does not know your opponent's
hand so even your _Best possible hand_ can be weaker than your opponent's hand and you will lose. It is your
job to read your opponent and make an assumption which cards he is holding.