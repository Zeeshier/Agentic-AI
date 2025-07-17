# Prompt Engineering: Advanced "Reasoning" Techniques

In this lesson, you'll learn three powerful "reasoning" techniques — **Chain of Thought**, **ReAct**, and **Self-Ask** — that dramatically improve LLM responses for complex tasks. You'll discover when and why to use each one, understand what's really happening under the hood (spoiler: it's not true reasoning), and see how these techniques fit naturally into your modular prompt framework from Lesson 1 as a new "reasoning strategy" component.

## Getting Better Answers from LLMs

Ask an LLM to solve a complex problem, and you might get a decent answer. Ask it to show its work first, and you'll often get a brilliant one.

That's the power of structured prompting—not just telling the model what to do, but guiding *how* to do it.

LLMs can handle complex tasks, but when prompted casually, they often skip steps, jump to conclusions, or give surface-level answers. Why? Because under the hood, these models aren't reasoning—they're predicting the next word in a plausible sequence. To get better outputs, we need better patterns.

This lesson introduces three such patterns—Chain of Thought, ReAct, and Self-Ask—that help LLMs perform deeper, more useful "reasoning" by nudging them into familiar, structured formats learned from human examples.

We'll explore:
- What each technique does and when to use it
- How to structure prompts that activate these reasoning patterns
- Why these techniques work, even though the model isn't really thinking
- How to plug them into your modular prompt framework from Lesson 1 as a new, configurable component: reasoning strategy

These aren't silver bullets, but when used well, they can transform your AI's behavior from shallow to strategic.

## The Three Reasoning Flows

Before we explore each technique in detail, let's visualize what we're actually doing when we apply these "reasoning" patterns. Each technique creates a different flow of text generation that mimics how humans approach different types of problems.

![Reasoning Flow](https://app-cdn.readytensor.ai/publications/resources/hubId=5489/publicationId=2453/reasoning-flow.svg?Expires=1752789336&Key-Pair-Id=K2V2TN6YBJQHTG&Signature=wpOuEb5433dg5G8E55qjb-F9fX~hdWU5vFlaQeKdQBz7gFnJ4WgNWI-~u6jTsMvDmWCRpDb~VyVp43xvhvswq23r5vkCMe9g0P1bQNfYqIToG2H~p7L-Q-lyQ-DQYBvyLBIa7HEOpvcRixu4GPS2G2qyszVuJfN2toHuY9b66kIHfoo8ikWUtMDQFwjqT56j1qgqF0IBJkp7OB2Q0ex6CAaSM8mupuveZuKwZvhUQnbJ~hqMB6mlWXYQUMWEjPt-YtlXOt2u-5cRcYxvI-3AE~8pxrYWrBhULX3KHLU0b8n~3xhYQ82F8qGET5yP~obENFDbKRb3ALYyiq0M8~PVxQ__)

Think of these as three different templates the LLM can follow, each optimized for different types of challenges:
- **Chain of Thought** follows a linear progression—break the problem down, work through each piece systematically, then synthesize. This mirrors how humans solve math problems or work through logical puzzles.
- **ReAct** cycles between thinking and doing—consider options, take action, observe results, reflect, then repeat. This matches how humans troubleshoot issues or navigate complex decisions with multiple variables.
- **Self-Ask** starts broad and narrows down—identify what you need to know, ask the right sub-questions, answer each one, then bring it all together. This reflects how humans approach research or analysis where the full scope isn't immediately clear.

The key insight? These aren't arbitrary structures. They're patterns the LLM learned from millions of examples of human problem-solving in text form—textbooks showing step-by-step solutions, technical documentation following troubleshooting procedures, and research papers breaking down complex questions.

When you use these techniques, you're not teaching the LLM to think. You're helping it access the most useful problem-solving patterns it has already learned.

Now let's see how each one works in practice.

## Chain of Thought (CoT)

Ever watched someone solve a math problem by talking through it step by step? That’s exactly what Chain of Thought does for LLMs. Instead of jumping straight to an answer, it prompts the model to break the problem into smaller parts and work through them logically.

This strategy was introduced in the 2022 paper *Chain of Thought Prompting Elicits Reasoning in Large Language Models* by Jason Wei et al. [Read it here](https://arxiv.org/abs/2201.11903).

### 🧠 When to Use It
Use CoT for:
- Multi-step problems
- Logical reasoning
- Analytical tasks
- Any situation where the path to the answer matters

It's also a good choice when you want to inspect or verify how the model arrived at its response.

### 💬 Prompt Text
**Simple Version**:
```
Let's think step by step.
```

**Detailed Version**:
```
Use this systematic approach to provide your response:
1. Break down the problem into smaller steps
2. Address each step systematically
3. Show your reasoning for each step
4. Then provide your final conclusion
```

### 🧪 Real Example
**Question**:
> Roger has 5 tennis balls. He buys 2 more cans of tennis balls. Each can has 3 tennis balls. Roger runs into his friend John. He gives John 3 tennis balls. How many tennis balls does he have now?

**Prompt**:
```
Let's think step by step.
```

**Response with Chain of Thought**:
```
Roger starts with 5 tennis balls.
He buys 2 cans, each with 3 balls: 2 × 3 = 6.
Total after purchase: 5 + 6 = 11.
He gives away 3 balls: 11 - 3 = 8.
Answer: Roger has 8 tennis balls.
```

### ⚠️ When CoT Might Not Work
- On simple tasks, it adds unnecessary verbosity
- For ill-defined problems, it can hallucinate plausible but wrong logic
- When misused, it can make bad answers sound more convincing

*Think about it*: Can you come up with a question where asking "let's think step by step" would actually make the response worse? What would that look like?

## ReAct (Reasoning + Acting)

Think of a detective solving a case: they don't just think through the clues—they act on their reasoning by gathering more evidence, then reason about what they found, then act again. That's ReAct in a nutshell: alternating between reasoning and taking actions to solve complex problems.

This approach was introduced in the 2022 paper *ReAct: Synergizing Reasoning and Acting in Language Models* by Shunyu Yao et al. [Read it here](https://arxiv.org/abs/2210.03629).

### 🧠 When to Use It
Use ReAct for:
- Problems that require external information or tools
- Research tasks that involve fact-finding or decision-making
- Multi-step workflows where intermediate results guide the next step
- Any situation where thinking alone isn’t enough

It's perfect when the model needs to search, calculate, or interact with external systems to solve a problem.

### 💬 Prompt Text
**Simple Version**:
```
Use this format: Thought (reason about what you need), Action (what you would do), Observation (what you would expect to find), then repeat until you can answer.
```

**Detailed Version**:
```
Use this systematic approach to provide your response:
1. Thought: What approaches could I take to solve this?
2. Action: Choose and implement the best approach
3. Observation: What happened? What did I learn?
4. Reflection: Do I have enough information to provide my final answer, or should I try a different approach?

(Repeat steps 1–4 as needed)

Then provide your final answer.
```

**LangChain Prompt Version**:
> Let's take a look at the prompt template for ReAct by Harrison Chase, creator of LangChain:
>
> ```
> Answer the following questions as best you can. You have access to the following tools:
>
> {tools}
>
> Use the following format:
>
> Question: the input question you must answer
> Thought: you should always think about what to do
> Action: the action to take, should be one of [{tool_names}]
> Action Input: the input to the action
> Observation: the result of the action
> ... (this Thought/Action/Action Input/Observation can repeat N times)
> Thought: I now know the final answer
> Final Answer: the final answer to the original input question
>
> Begin!
>
> Question: {input}
> Thought:{agent_scratchpad}
> ```
> Source: [hwchase17/react](https://github.com/hwchase17/react)

This format assumes tool use (which we'll cover soon), but the core ReAct pattern, which is Think → Act → Observe → Reflect, is already clear from the structure.

### 🧪 Real Example
**Question**:
> What's the current population of the capital city of the country that won the most recent FIFA World Cup?
>
> Use this format: Thought (reason about what you need), Action (what you would do), Observation (what you would expect to find), then repeat until you can answer.

**Response with ReAct**:
```
**Thought:** I need to identify which country won the most recent FIFA World Cup, then find their capital city, and finally get the current population of that capital.

**Action:** Determine the winner of the most recent FIFA World Cup.

**Observation:** The most recent FIFA World Cup was held in Qatar in 2022, and Argentina won the tournament, defeating France in the final.

**Thought:** Now I know Argentina won the 2022 World Cup. Next, I need to identify Argentina's capital city.

**Action:** Identify the capital of Argentina.

**Observation:** The capital of Argentina is Buenos Aires.

**Thought:** Now I need to find the current population of Buenos Aires. Since population data changes and I want the most current figures, I should search for this information.

**Action:** Search for the current population of Buenos Aires.

**Observation:** I found current population data for Buenos Aires. The search results show some variation in the figures, but the most current and consistent data indicates that the Buenos Aires metropolitan area has a population of approximately 15.75 million people as of 2025.

**Thought:** I now have all the information needed to answer the question. Let me synthesize the findings.

**Final Answer:** The current population of Buenos Aires (the capital city of Argentina, which won the 2022 FIFA World Cup) is approximately 15.75 million people in the metropolitan area as of 2025. The city proper has about 3.1 million residents, while the urban area encompasses 16.7 million people, making it one of the largest metropolitan areas in South America.
```

### ⚠️ When ReAct Might Not Work
- For simple questions that don't require external information
- Can create fake "actions" that look convincing but didn't actually happen

*Think about it*: Can you spot a question where ReAct would just be pretending to take actions without actually doing anything useful?

## Self-Ask

Imagine breaking a tough question into smaller, easier ones—then answering each one before putting the full picture together. That’s Self-Ask: a strategy where the model generates sub-questions, answers them one by one, then synthesizes a final answer.

### 🧠 When to Use It
Use Self-Ask when:
- Problems require solving smaller, easier sub-problems first
- You need to explore multiple angles before deciding
- The task benefits from explicit decomposition

It’s great for anything that needs a “let’s break this down” approach.

### 💬 Prompt Text
**Simple Version**:
```
To answer this question, what sub-questions should I ask first? Answer each one, then provide a final conclusion.
```

**Detailed Version**:
```
Use this systematic approach to provide your response:
1. Break the main question into smaller sub-questions.
2. Answer each sub-question thoroughly.
3. Then, based on those answers, synthesize a clear and thoughtful final response.
```

**LangChain Example**:
> Let's review Harrison Chase's Self-Ask prompt template from LangChain:
>
> ```
> Question: Who lived longer, Muhammad Ali or Alan Turing?
> Are follow up questions needed here: Yes.
> Follow up: How old was Muhammad Ali when he died?
> Intermediate answer: Muhammad Ali was 74 years old when he died.
> Follow up: How old was Alan Turing when he died?
> Intermediate answer: Alan Turing was 41 years old when he died.
> So the final answer is: Muhammad Ali
>
> Question: When was the founder of craigslist born?
> Are follow up questions needed here: Yes.
> Follow up: Who was the founder of craigslist?
> Intermediate answer: Craigslist was founded by Craig Newmark.
> Follow up: When was Craig Newmark born?
> Intermediate answer: Craig Newmark was born on December 6, 1952.
> So the final answer is: December 6, 1952
>
> Question: Who was the maternal grandfather of George Washington?
> Are follow up questions needed here: Yes.
> Follow up: Who was the mother of George Washington?
> Intermediate answer: The mother of George Washington was Mary Ball Washington.
> Follow up: Who was the father of Mary Ball Washington?
> Intermediate answer: The father of Mary Ball Washington was Joseph Ball.
> So the final answer is: Joseph Ball
>
> Question: Are both the directors of Jaws and Casino Royale from the same country?
> Are follow up questions needed here: Yes.
> Follow up: Who is the director of Jaws?
> Intermediate answer: The director of Jaws is Steven Spielberg.
> Follow up: Where is Steven Spielberg from?
> Intermediate answer: The United States.
> Follow up: Who is the director of Casino Royale?
> Intermediate answer: The director of Casino Royale is Martin Campbell.
> Follow up: Where is Martin Campbell from?
> Intermediate answer: New Zealand.
> So the final answer is: No
>
> Question: {input}
> Are followup questions needed here:{agent_scratchpad}
> ```
> Source: [hwchase17/self-ask-with-search](https://github.com/hwchase17/self-ask-with-search)

Note this template is using few-shot examples to show how to break down the question and answer it step by step. The model is prompted to think about whether follow-up questions are needed, then generate those questions and their answers.

### ⚠️ When Self-Ask Might Not Work
- Simple, direct questions that don't need decomposition
- When sub-questions become more complex than the original question
- Can create unnecessary overhead for straightforward tasks

*Think about it*: What’s a situation where breaking the question down would make the response worse, not better?

## Reality Check: Can LLMs Really Reason?

When we say an LLM is using "reasoning" techniques, we need to be honest about what's actually happening under the hood. These models aren't thinking, deliberating, or having insights. They're sophisticated pattern-matching systems performing structured text generation. Let's not forget that modern LLMs are still just doing next-word (token) prediction.

### So, Why Do These Techniques Work So Well?

#### The Training Data Connection
The answer lies in what LLMs learned during training. They've encountered millions of examples of humans using these exact patterns in written text:
- **Chain of Thought**: Math textbooks, tutorial explanations, step-by-step guides where humans write "First... then... therefore..."
- **ReAct**: Technical documentation, troubleshooting guides, research methodologies that follow "assess the situation → take action → evaluate results"
- **Self-Ask**: Academic papers, investigative journalism, educational content that breaks complex topics into sub-questions

When you prompt an LLM to use these techniques, you're not teaching it to reason. You're triggering specific patterns of sequential text generation from the LLM that mimics human reasoning found in its training data (i.e., all the text on the internet).

The key: solutions to problems of different types were explained (reasoned) using different patterns in the literature. Match your reasoning technique to your problem type, and you dramatically improve results. Mismatch them, and you might get worse answers than prompting directly.

### The Practical Implications
Understanding this reality helps you use these techniques more effectively:
- **For optimization**: If a reasoning technique isn't working, ask "What pattern am I trying to trigger?" rather than "Why isn't it thinking properly?"
- **For expectations**: These techniques make outputs more structured and thorough, but they don't guarantee correctness. The LLM can still hallucinate confidently within any reasoning framework.

*Deep question*: If LLMs are just mimicking human reasoning patterns they learned from text, what does that suggest about the nature of human reasoning itself?

The bottom line: These "reasoning" techniques are incredibly useful tools for generating better, more structured outputs. Just remember you're working with very sophisticated pattern matching, not actual thought.

## Integration with Modular Prompts

Remember the modular prompt framework from the last lesson? These reasoning techniques integrate easily as a new *reasoning strategy* component.

Let's take our publication summarization example from Lesson 1 and add Chain of Thought reasoning:

**Original prompt structure**:
- Role: AI communicator for general audience
- Task: Summarize publication
- Constraints: Single paragraph, 80-100 words
- Style: Plain language, no jargon
- Goal: Help readers decide if worth reading

**Adding Chain of Thought processing**:
Simply insert this in your prompt as shown below:

![Modular Prompt with CoT](https://app-cdn.readytensor.ai/publications/resources/hubId=5489/publicationId=2453/modular-prompt-with-CoT-v2.svg?Expires=1752789336&Key-Pair-Id=K2V2TN6YBJQHTG&Signature=u56YKfp~WKgMW2rjEKat2ZVtjQ62kaw~88mAbprWXoBOS4Il-hZmtI0gz8OnY0ugcdIW9zgJI75ztPzZoBh430yXVJSlAn~PMs4ubVI8MRp7X~9fnGlo1tctALOv4o03y0Bqt6BhI3m43H2NOzyZ0F4NWrYJ64yE9APl0CW4oSKHoIm2JNiQ7cNvjoRDIldEZ3rIvfcAnQyVahu5NkvFi3Gv7U39FSzp4NKSR5hwUojCRmEjDcPh7-6v3BvoKmBKuYK0fR5WqdMLdh5NE9tHmkbOv55TL-AwjsdxV793bOsuhoEWsJKJ~0JE2lHjUcIgXJH9dSfZ8GNOjtQ~pVfQ2Q__)

We are choosing CoT out of the three strategies because our summarization task benefits from step-by-step thinking: understanding content, identifying key points, then synthesizing for the target audience.

**The key insight**:
These reasoning strategies slot in as a new modular component, giving you control over how the LLM processes your task while keeping all other elements unchanged.