# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it? The interface looked fine at first glance - the layout loaded correctly and the inputs/buttons appeared to work. However, after actually playing a few rounds, I noticed logic errors that made the game behave differently than expected. When I clicked the guess/submit button, the feedback and game state didn’t match the intended response, so the gameplay felt inconsistent and unreliable.
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

  1 I expected the hint to correctly guide the player toward the secret number (for example, showing “Go higher” when the guess is too low). However, the game sometimes showed the opposite instruction, which made the hints confusing and incorrect.

  2 I expected the score to reset to its initial value when starting a new game. Instead, the score remained the same, even after clicking the New Game button.

  3 I expected the New Game button to reset the game and generate a new secret number after winning. Instead, nothing happened when the button was pressed, and the game did not restart.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? ChatGPT
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
