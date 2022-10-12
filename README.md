# Roulette Strategy Simulator
This python program tests if a particular roulette strategy gives you a noticeable greater edge at all. In short the answer is no.

After manually calculating the odds in a spreadsheet it still didn't make tangible sense to me so I decided to write this little program to play the games for me.

## The Strategy
Very simply you bet on the three 2 to 1 areas, red or black, odd or even, 1 -18 or 19 - 36.
To keep things interesting you change your bet to match the number that just came up
For example, if the number was 7 the next bet would be red, odd, 1 - 18
then say it was 15 you would keep the odd, and  1 -18, and change to black

## The Results
The results form the program matched my calculated odds on average
| Result      | Odds   |
| ----------- | ------ |
| No Bets Win | ~14.5% |
| 2/3rd Back  | ~37%   |
| 2 to 1 win  | ~37%   |
| 3 to 1 win  | ~11.5  |

These odds are not enough to beat the system, starting with $100, over a long enough time you lose it all.


