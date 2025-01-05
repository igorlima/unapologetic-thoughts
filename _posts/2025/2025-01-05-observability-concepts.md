---
layout: post
title: Observability Concepts
category: technical
---

- **Traces:** A trace provides a view of how a request travels through a
  distributed system. For example, it might show the journey of a request as it
  moves from the front end to the back end, interacts with a database, and
  returns to the front end. This helps identify bottlenecks or failure points
  across different components. [^1]
- **Spans:** A span represents a single operation within a trace, with
  information on when the operation started and ended. Spans are the building
  blocks of a trace, as each span details an individual step within the
  request’s journey, enabling precise insights into which part of the process
  might be lagging.
- **Metrics:** Metrics can represent anything quantifiable within the system,
  such as the request processing time or the number of requests over a period.
  Metrics are crucial for tracking performance trends over time and can help
  detect unusual behavior, like a sudden spike in response times or request
  volume.

---
{: data-content="footnotes"}

[^1]: [Keeping Your AI Agent in Check: An Introductory Guide to Traces, Metrics and Logging](https://towardsdatascience.com/keeping-your-ai-agent-in-check-an-introductory-guide-to-traces-metrics-and-logging-a731b57b8658)
