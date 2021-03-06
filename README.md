# Three Card Poker #

*This program was written in Python 2.7 using PyCharm*

**Functionality**

This program takes in as input a block of text involving: the number of players on the first line and a player id and value of each of their three cards on each subsequent line. It outputs the winner(s) of the match in one line.

*This program expects exact input as specified. It does not check for blank or incorrectly formatted input.*

**Specific Implementation Details**

To calculate the value of a player's hand this program converts each card in the player's hand into an integer, calculates the strength of the player's hand using the integer values of each card. The integer representation of each card represents the strength of that card relative to other cards. The integer part of the floating point number represents the player's hand combination and the decimal part of the floating point number represents the strength of that combination relative to other players with the same combination.

**Card Format**

Cards are a string of length 2. The first character represents the rank of the card, it can represent a number or a letter. The second character represents the suit of the card.

*Example* <br/>
"Kd" is the King of Diamonds <br/>
"2c" is the 2 of Clubs

**Input Format**

Number of Players <br/>
PlayerID Card1 Card2 Card3

**Test Cases**

*Example 1* <br/>

Input: <br/>
3 <br />
0 2c As 4d <br/>
1 Kd 5h 6c <br/>
2 Jc Jd 9s <br/>

Output: 2

*Example 2* <br/>

Input: <br/>
3 <br/>
0 Kh 4d 3c <br/>
1 Jd 5c 7s <br/>
2 9s 3h 2d <br/>

Output: <br/>
0
