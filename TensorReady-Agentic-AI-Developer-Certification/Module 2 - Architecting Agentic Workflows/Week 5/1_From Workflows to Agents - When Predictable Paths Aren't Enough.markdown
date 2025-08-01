# From Workflows to Agents: When Predictable Paths Aren't Enough

## TL;DR

Learn when to move beyond predictable LLM workflows toward more dynamic agent-based systems. This lesson breaks down the spectrum between static workflows and adaptive agents — and shows how to choose the right level of flexibility for your use case.

## What We've Built So Far 🛠️

In Module 1, you built impressive assistants using:

- Making basic LLM calls
- Multi-turn conversations
- Memory (including persisted memory)
- Vector databases
- Retrieval-augmented generation (RAG)

What's even more remarkable: we accomplished all of this without any tools, and without any agents. Just LLMs, retrieval, and smart prompting.

These systems were powerful — and also predictable. Your RAG assistant followed a consistent path:

![Query-Retrieve-Respond](https://app-cdn.readytensor.ai/publications/resources/hubId=5489/publicationId=2785/query-retrieve-respond-v3.jpg?Expires=1754089999&Key-Pair-Id=K2V2TN6YBJQHTG&Signature=Exfw1nOGnnhTobWgw3ufHnEatbIceQS-aC3ZsO-Ah4Rpr0mgXM-ODJo5uesoUcjxIh25Bo~Lj2wF4fMhXxfNOdx68cFJZxJ01qP-mmliDzBFhKi5-1-MkK9aTWdAQNNtf9VcT1a~yCskxFFDUusBb6Ozhtpun14ujjLoWGhOMvPU5OW3SB2rWlinXyGspSwirOI3Ay0JdpLMVYwa6BjMtOL5Gh0yNFO6u2hDb1g6Vo-~1oSqfBE3ayc-nJ7~NARE9KxJRvGUD7NpUNJKRXHOZbocmEiRD2u-6e1zRsF0wgH793z0BWFtzniOHNMluYGiOYx0WGHAdUqJwp1GDUCWXg__)

That predictability is a feature. It makes your system easy to debug, easy to monitor, and cost-effective to run.

But such predictability comes at a cost: the system only works when the path is known in advance.

## Limitations of Pre-Defined LLM Workflows

You’ve built a solid RAG assistant. It answers user questions about your publications — efficiently, predictably. You’re feeling good.

Then your manager walks in and says:

> "Users are starting to ask more complex questions. Like — Is the technique in this publication actually state-of-the-art? Can we cross-reference with arXiv or other sources?"

You say "No problem." You add a router that detects questions needing external info. If needed, it hits an API to fetch fresh data. Your workflow just got a little more… conditional.

A few days later:

> “Now they want stats. What percentage of our RAG implementations use Chroma DB?”

Hmm... 🤔 This needs you to scan all relevant publications, extract metadata, and compute an aggregate.

So you add another if-then branch and build a fan-out loop — scan documents, extract info, tally the results.

It’s not elegant, but it works. The system now handles more complex aggregation queries.

Next day, your manager makes another request:

> “Users are starting to ask for comparisons. Like — How are transformer models being used across our computer vision projects? Can we group them and highlight what’s different?”

Okay. You sigh. This is turning into a nested workflow jungle 😓 — branching logic, map-reduce flows, specialized handlers everywhere.

It still works. But every new request adds more logic. Your once-elegant system is starting to resemble spaghetti.

Then comes the final blow:

> “Users are asking open-ended questions. Like: What are the most important insights across these 500 new publications? Extract trends — by industry, by technique, by framework. Summarize what people are doing well. Suggest areas for improvement. Can we support questions like these?”

You stare at your branching workflow, your routers and mappers, your conditional flags ... And you realize:

❗ This is no longer a workflow problem — because you can’t even predict the paths anymore.

You don’t need another if-else.

You need a system that can adapt, plan, delegate, analyze, critique, and synthesize — all in response to open-ended goals.

You need a system that can choose its own next steps. A system that makes decisions, uses tools, explores unknowns, and coordinates across tasks.

That’s the shift — from a predictable, static workflow… to a dynamic, agent-based system.

## Dynamic, Agent-Based Systems 🧠

At this point, you might be wondering: We’ve mentioned agents and agentic or agent-based systems… but what exactly makes something an agent?

Let’s start with a simple definition from Hugging Face:

> “AI agents are systems where LLM reasoning determines the next steps in a dynamic workflow.”

In other words, instead of just following a fixed script, the system decides what to do next based on what it just discovered.

### So What Makes a System Agentic? 🤖

![Agentic System](https://app-cdn.readytensor.ai/publications/resources/hubId=5489/publicationId=2785/agentic-system3.jpg?Expires=1754089999&Key-Pair-Id=K2V2TN6YBJQHTG&Signature=TSTrLAc6nOqdB4-NDNqOXSvngBpJu2qo5xUtWqNJ-OTQW5GlqjEiYgTaqT7RY4mgPLhbOE2VsAyhdD9UqXu2HNPK94iAXV6LEEYUzVjTbbilqq2K3Bi~Wt6xuTvtABmsm5Rb-DzqUcxnoivChyKrmhl3HtjwQEWTG1jr~su326i1cb1kMykKxTUZXRPT7ib3uAFaDrFbg6g8YfwDY8~PTZXba2xUb5O8FcIoYP9a2NMgM5RZsdkcjh8xTznbn6JrePD38aowAdzVhe8H~PbaZuMcVHhziXSyW4IZC6Ib92bIjtjjZb1rF7xgHmg6mH6L1p2PxOcC4zhhWJpNWSssSw__)

Agentic systems typically include:

- ✅ Multiple LLM calls, not just one-shot answers
- 🔧 Tool use to search, calculate, write, fetch, or manipulate
- 🧠 A reasoning loop that can reflect and revise
- 🧭 A planner or controller to coordinate what happens when
- 🎯 Autonomy — it decides how to achieve the goal

More broadly, these systems don’t just respond — they can plan and take flexible sequences of actions to achieve a goal, adapting their course based on the needs of the task.

### Let’s Connect Back to Your RAG Assistant 📚

Remember your assistant from Module 1? It followed a clear, fixed path: query → retrieve → respond

Now imagine an agentic version of that assistant:

- It sees your question and says, “Hmm, this might need external info.”
- It decides to search arXiv — or maybe checks an internal knowledge base first.
- It pulls multiple sources, weighs them, and even evaluates which is more up-to-date.
- If unsure, it clarifies the user’s intent before answering.
- At every step, the LLM decides what to do next.

That’s the shift from a workflow… to a truly agentic system.

## It’s a Spectrum, Not a Switch ⚖️

It’s tempting to think of workflows and agents as two separate categories — one static and rule-based, the other dynamic and autonomous. But in practice, that distinction isn’t so clean.

Most real-world systems fall somewhere in between.

You might have a mostly predictable flow with just one agentic step:
- → “Check if user intent is unclear. If so, ask a clarifying question.”

Or you might go further:
- → “Decide whether to retrieve from memory, search externally, or ask the user to rephrase — based on what we’ve seen so far.”

Agentic behavior exists on a spectrum. The more flexibility you introduce, the more autonomy the system has — and the more powerful it becomes.

But there's a catch.

## Agentic Flexibility Comes at a Cost ⚠️

It’s easy to fall in love with the idea of a fully autonomous, open-ended agent that can figure out anything, route any request, and call any tool.

![Agentic System Drawbacks](https://app-cdn.readytensor.ai/publications/resources/hubId=5489/publicationId=2785/agentic-system-drawbacks.jpg?Expires=1754089999&Key-Pair-Id=K2V2TN6YBJQHTG&Signature=Z5Umcs2ImlY-BwFn~XD~jVDX-Pm5y2w3ZFh4bmEK5j76MfRO2oxJT4EuFHxsJpbYwIYoYiu~DTlH0ucr1Y3XoyTWxcQ2Powu~ls7A8GntVYQYU61gRnWe1O4XSm347ulWRqfiHXoIy8b7DsP1kRYbQ0eVsGzYiW1VWqIoZw-dGSMRX5UvXHdvsMlR6FVEUaybwJm6atxK4M9BBiIK5g7cd3ALyjTFc3VJ1mCWqn25CAaxO-pjXoLDA2lrSDwO4j2X~Sjwrta3F86fKM1qY2se484fb8m1FWllYlexY7QUmnk5X7h09~8S5lMQa6GrwW3Z0M8A7KdpKuYZ7C3t5MucQ__)

But highly flexible systems come with hidden costs.

They’re harder to test, less predictable in their behavior, more expensive to run, and notoriously tricky to debug when things go wrong. What feels like intelligent autonomy in a demo can quickly become unmanageable in production — especially when workflows loop, branch, or trigger unexpected tool usage.

Just because you can make something dynamic doesn't mean you should.

Let’s go back to that last request from your manager:

> “Users are asking open-ended questions. Like: What are the most important insights across these 500 new publications? Extract trends — by industry, by technique, by framework. Summarize what people are doing well. Suggest areas for improvement. Can we support questions like these?”

Sounds like a dream use case, right? But before you rush to build a massively dynamic multi-agent system with autonomous planning and open-ended synthesis… pause.

Ask yourself:

- Is this even feasible?
- Can we support this reliably, not just theoretically?

Maybe it's enough to extract key tags. Maybe “I don’t know” is the right answer for certain complex queries — not a flaw.

Remember, agentic design isn’t about chasing autonomy. It’s about building systems that adapt when needed, while staying grounded in reliability and control.

Start with the simplest version that meets your needs. Add flexibility only when it solves a real problem — not just because it sounds impressive.