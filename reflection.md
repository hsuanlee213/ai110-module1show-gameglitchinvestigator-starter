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

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
-
- ChatGPT and copilot
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

  For 'if guess > secret:' return in app.py, AI suggests : Message is reversed here. When guess > secret the player should be told to go LOWER (because their guess is too high). The return value currently says "Too High" correctly, but the message text "Go HIGHER!" is incorrect. Which is obvious when reading the corresponding code section.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

  At first glance, I did not see any suggestions that were incorrect or misleading. However, if I want to refactor the code or make my own arrangement, I will need to give more specific instructions on how to refactor the existing code.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  I run the game after each fix to make sure it reflects my updated code logic.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

  I used copilot to run the pytest for the logic of score text (go higher / go lower). It shows result match.

- Did AI help you design or understand any tests? How?

  It helps me quickly identify where the logic error is, and it helps me quickly adjust to

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
  Streamlit reruns the entire script whenever a user interacts with the app, so important values must be stored in st.session_state. In the original app.py, the secret number was initialized correctly, but it was later reset or converted to a string in other parts of the code. Converting the secret to a string caused lexicographic comparisons instead of numeric comparisons (for example, "9" > "10"), which led to incorrect hints and inconsistent behavior. To fix this, I moved the comparison logic into logic_utils.check_guess and ensured all comparisons use numeric values. I also removed the string conversion and updated the New Game logic to reset secret, attempts, score, status, and history together, ensuring the game state remains consistent.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  In Streamlit, the whole program runs again every time the user interacts with the app, like pressing a button or submitting a guess. This is called a “rerun.” If we only use normal variables, their values would reset each time the program reruns. To solve this, Streamlit provides st.session_state, which acts like memory for the app. It stores important values so they stay the same across interactions, even though the script keeps running again.
- What change did you make that finally gave the game a stable secret number?
  The change that finally gave the game a stable secret number was ensuring that the secret value was stored and managed correctly in st.session_state. I removed the code that converted the secret number to a string and made sure it was always treated as an integer. I also ensured that the secret number is only initialized when "secret" is not already in st.session_state. This prevents the value from being reset during Streamlit reruns, allowing the secret number to remain stable throughout the game.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
    One strategy I want to reuse is making small changes and pushing them to GitHub frequently so that progress is tracked and mistakes can be easily reversed. I also learned to use the @codebase context in Copilot to help the AI understand the full project when suggesting fixes.
- What is one thing you would do differently next time you work with AI on a coding task?
  Next time, I would give more specific prompts when working with AI. AI can sometimes modify a large amount of code from a very small instruction, so focusing on a smaller section of the code and clearly describing the task can help keep the changes more controlled and easier to review.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  This project showed me that AI-generated code can be helpful and often high quality, but it still requires careful review. It is important to understand the logic behind the code instead of relying on AI completely.
