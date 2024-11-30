### Poker Hand Probabilities/674b227d-11c8-8012-ac6d-bb04699bc30f

In a standard game of **Texas Hold'em** or **Five-Card Draw Poker**, the deck consists of 52 cards, and probabilities for specific hands depend on the combinations of cards in a dealt hand.

Below are the probabilities of each poker hand in a five-card hand:

| **Hand**           | **Frequency** | **Probability**      | **Odds Against**   |
|---------------------|---------------|-----------------------|--------------------|
| **Royal Flush**     | 4             | $$0.000154\%$$      | 649,739 to 1       |
| **Straight Flush**  | 36            | $$0.00139\%$$       | 72,192 to 1        |
| **Four of a Kind**  | 624           | $$0.024\%$$         | 4,164 to 1         |
| **Full House**      | 3,744         | $$0.144\%$$         | 693 to 1           |
| **Flush**           | 5,108         | $$0.197\%$$         | 508 to 1           |
| **Straight**        | 10,200        | $$0.39\%$$          | 254 to 1           |
| **Three of a Kind** | 54,912        | $$2.1128\%$$        | 46.3 to 1          |
| **Two Pair**        | 123,552       | $$4.7539\%$$        | 20.0 to 1          |
| **One Pair**        | 1,098,240     | $$42.2569\%$$       | 1.37 to 1          |
| **High Card**       | 1,302,540     | $$50.1177\%$$       | 0.995 to 1         |

---

### Key Concepts

- **Royal Flush**: Ace, King, Queen, Jack, and 10 of the same suit.
- **Straight Flush**: Five consecutive cards of the same suit (not Royal).
- **Four of a Kind**: Four cards of the same rank (e.g., four Kings).
- **Full House**: Three cards of one rank and two cards of another (e.g., three Aces and two Kings).
- **Flush**: Five cards of the same suit (not in sequence).
- **Straight**: Five consecutive cards of mixed suits.
- **Three of a Kind**: Three cards of the same rank.
- **Two Pair**: Two different pairs of cards.
- **One Pair**: Two cards of the same rank.
- **High Card**: None of the above combinations; the hand's value is determined by the highest card.

---

### Calculation Insights

These probabilities are derived from **combinatorics**:

- The total number of possible five-card hands:
  
$$
\binom{52}{5} = \frac{52!}{5!(52-5)!} = 2,598,960
$$

Each specific hand type is calculated based on the ways to select cards to form that hand divided by the total number of hands.

For example:

- Royal Flush:

$$
\binom{4}{1} = 4
$$

(Only 4 Royal Flushes are possible, one per suit.)

- Four of a Kind:

$$
\binom{13}{1} \times \binom{12}{1} \times \binom{4}{4} \times \binom{48}{1} = 624
$$

You can adjust calculations for other poker variants or include probabilities for community cards in **Texas Hold'em**. Let me know if you'd like to explore this further!

Let's break down the calculation for **Four of a Kind** to understand why $` \binom{13}{1} \times \binom{12}{1} \times \binom{4}{4} \times \binom{48}{1} = 624 `$:

---

### **What is Four of a Kind?**

A **Four of a Kind** is a poker hand consisting of:

- Four cards of the same rank (e.g., four Kings: $` \heartsuit K, \clubsuit K, \spadesuit K, \diamondsuit K `$),
- One additional card of any rank (not matching the four of a kind).

---

### **Breaking Down the Calculation**

1. **Choose the Rank for the Four of a Kind: $` \binom{13}{1} `$**
   - There are 13 possible ranks ($` \text{A, 2, 3, ..., K} `$).
   - We need to choose **one** rank for our Four of a Kind.

 $$
 \binom{13}{1} = 13
 $$

2. **Choose the Rank for the Additional Card: $` \binom{12}{1} `$**
   - After selecting the rank for the Four of a Kind, 12 ranks remain for the fifth card.
   - We need to choose **one** of these remaining ranks.

 $$
 \binom{12}{1} = 12
 $$

3. **Choose All Four Suits for the Four of a Kind: $` \binom{4}{4} `$**
   - For the Four of a Kind, we need all four suits (e.g., $` \heartsuit, \clubsuit, \spadesuit, \diamondsuit `$).
   - There is only **one way** to choose all four suits:

 $$
 \binom{4}{4} = 1
 $$

4. **Choose One Card from the Remaining Deck: $` \binom{48}{1} `$**
   - After selecting the four cards of the same rank, 48 cards remain in the deck.
   - We need to choose **one** card to complete the hand.

 $$
 \binom{48}{1} = 48
 $$

---

### **Combining These Choices**

The total number of ways to form a **Four of a Kind** hand is:

$$
\binom{13}{1} \times \binom{12}{1} \times \binom{4}{4} \times \binom{48}{1}
$$

Substitute the values:

$$
13 \times 12 \times 1 \times 48 = 624
$$

---

### **Why Does This Work?**

This formula counts all possible ways to form a valid Four of a Kind hand:

1. First, choose the rank for the Four of a Kind ($` 13 `$ choices).
2. Then, choose the rank for the kicker (the additional card, $` 12 `$ choices).
3. Next, select all four suits for the Four of a Kind ($` 1 `$ way).
4. Finally, pick one card from the remaining deck ($` 48 `$ ways).

This ensures all valid combinations are counted without overcounting or missing any possibilities. 

Let me know if you'd like more assistance!
