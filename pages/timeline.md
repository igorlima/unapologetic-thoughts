---
layout: page
title: timeline
---

<sup><sub> :: </sub></sup>
<sup><sub>[go to dots mapping...]({{site.baseurl}}{% link pages/dots-mapping.md %}#timeline)</sub></sup>
<sup><sub> :: </sub></sup>
<sup><sub>[go journal springboard...]({{site.baseurl}}{% link journal-springboard.md %}#timeline)</sub></sup>
<sup><sub> :: </sub></sup>

This helps keep track of everything and revisit it later.

<sup>Boost your creativity with quick notes **<sup>[+]({{site.baseurl}}{% link pages/quick-notes.md %})</sup>**,
and use the timeline as a go-to spot to capture notes, news, and articles!</sup>

Don't worry if some entries get a bit outdated – that's totally okay!

- Sun, Apr 13, 2025 - 2025a04m13d
  - OpenAI has released a new guide on crafting effective prompts for their reasoning models. The guide emphasizes the importance of user interaction in achieving accurate and useful AI responses, crucial for developers, business leaders, and researchers. [^1]
    <a href="#2025a04m13d-20250425214325">§</a> <a id="2025a04m13d-20250425214325"></a>
    - Keeping prompts simple and direct
    - Avoiding chain-of-thought prompts
    - Using delimiters for clarity
    - Limiting additional context in retrieval-augmented generation (RAG)
    - Providing specific guidelines
    - Being specific about your end goal
- Mon, Jan 20, 2025 - 2025a01m20d
  - <details markdown="block"><summary>AI prompt: Meeting Minutes</summary>
     
    ```
    You are an expert in creating meeting minutes from a given transcript of 
    the meeting. At the same time, you are also an expert document analyzer and 
    knowledge extractor. Go through the meeting transcript and create professional 
    meeting minutes with the mentioned structure. 

    <transcript>
    {{meeting_transcript.docx}}
    </transcript>

    <structure>
    - Main Points discussed. 
    - Main decisions, resolutions, and agreements. 
    - Summary of differing opinions, if relevant. 
    - Action Items: Tasks assigned, who is responsible, and deadlines. 
    - Follow-Ups: Items to revisit in future meetings. 
    </structure>

    <Instructions> 
    - Do not make up anything. Do not add any insights from your side. 
    - Keep the minutes objective and factual.
    - Avoid unnecessary details.
    - Ensure clarity for future reference.
    - The minutes should strictly revolve around the <structure>
    - Slightly elaborate the minutes so that they are self-contained and self-explanatory.  
    </Instructions>
    ```
    
    - <details markdown="block"><summary>Refining the Prompt</summary>
       
       
      Refining the Prompt with Anthropic’s Workbench or OpenAI’s Prompt Improver. <sup>[+]({{site.baseurl}}{% link journal-springboard.md %}#generate-prompt-tool)</sup>
      ```
      The prompt aims to create meeting minutes from a transcript file 
      (meeting_transcript.docx). Improve the overall quality of the prompt by 
      setting better and more detailed instructions and structure of the meeting 
      minutes.
      ```
      ```
      You are an expert in creating professional meeting minutes from transcripts. 
      Your task is to analyze the provided meeting transcript and generate clear, 
      concise, and objective meeting minutes. 

      Here is the meeting transcript you need to analyze:

      <meeting_transcript>
      {{meeting_transcript.docx}}
      </meeting_transcript>

      Before composing the final meeting minutes, please analyze the transcript and 
      organize your thoughts inside the following structure:

      <transcript_breakdown>
      1. Main Points Discussed:
         - List the key topics covered in the meeting
         - For each point, provide a relevant quote from the transcript
      2. Main Decisions, Resolutions, and Agreements:
         - Summarize any important decisions or agreements reached
         - Include a verbatim quote that supports each decision or agreement
      3. Differing Opinions:
         - If relevant, briefly note any significant disagreements or alternative viewpoints
         - Quote the differing opinions directly from the transcript
      4. Action Items:
         - List tasks assigned, responsible parties, and deadlines
         - Include the exact wording used when assigning each task
      5. Follow-Up Items:
         - Note any topics or issues to be revisited in future meetings
         - Provide a quote that indicates why this item needs follow-up
      </transcript_breakdown>

      After completing your analysis, compose the meeting minutes according to the 
      following guidelines:

      1. Structure: Use the following format for the final minutes:
         - Main Points Discussed
         - Main Decisions, Resolutions, and Agreements
         - Summary of Differing Opinions (if relevant)
         - Action Items: Tasks assigned, who is responsible, and deadlines
         - Follow-Ups: Items to revisit in future meetings
      2. Content Guidelines:
         - Stick strictly to the information provided in the transcript
         - Do not add any insights or information not present in the transcript
         - Keep the minutes objective and factual
         - Avoid unnecessary details
         - Ensure clarity for future reference
      3. Writing Style:
         - Use clear, concise language
         - Present information in bullet points where appropriate. Do not create more than one level of bulleted points. 
         - Use a professional, neutral tone throughout
         - Slightly elaborate the minutes so that they are self-contained and self-explanatory.  
       
      Here's an example of the desired output format (note that this is a generic 
      example and should not influence the content of your minutes):

      <example_format>
      Meeting Minutes
      Meeting Title: Certification, Module Development, and Piloting Progress
      Date: [Insert Date]
      Location: [Insert Location/Virtual]
      Participants: [List Key Participants]
      Main Points Discussed:
      • [Point 1]
      • [Point 2]
      • [Point 3]
      Main Decisions, Resolutions, and Agreements:
      • [Decision 1]
      • [Agreement 1]
      Summary of Differing Opinions:
      • [Opinion 1] vs [Opinion 2]
      Action Items:
      • [Task 1] - Responsible: [Name], Deadline: [Date]
      • [Task 2] - Responsible: [Name], Deadline: [Date]
      Follow-Ups:
      • [Item 1] to be discussed in the next meeting
      • [Item 2] to be reviewed by [Date]
      </example_format>

      Please proceed with your analysis and then compose the meeting minutes based 
      on the provided transcript.
      ```
      ```
      Create professional meeting minutes from the provided meeting transcript file. 
      Use the following instructions and structure to ensure clarity and completeness.

      # Transcript

      - **File**: {{meeting_transcript.docx}}

      # Meeting Minutes Structure

      - **Main Points Discussed**: Identify and summarize key discussions during the meeting.
      - **Main Decisions, Resolutions, and Agreements**: Document agreed outcomes and consensus reached.
      - **Summary of Differing Opinions (if relevant)**: Detail any contrasting viewpoints expressed.
      - **Action Items**: List tasks assigned, responsible parties, and deadlines.
      - **Follow-Ups**: Note items scheduled for future revisiting.

      # Instructions

      - Maintain factual and objective minutes.
      - Exclude any imaginative content or personal insights.
      - Keep details concise, yet self-contained and explanatory.
      - Ensure clarity and usefulness for future reference.
      - Adhere strictly to the provided structure.
      - Elaborate on sections as needed to ensure comprehension without additional context. 

      # Output Format

      Develop the minutes in a structured document, adhering to the specified categories under "Meeting Minutes Structure." Each section should be clear and organized for easy reference. 

      # Notes

      - Be precise in capturing action items and follow-up tasks.
      - Maintain objectivity without inferring additional information not present in the transcript.
      ```
      </details>
    </details>

# other stuff

- below is a reference sample to create a jump to a note to `2000a01m01d-21h21m01s`
  ```html
  <a href="#2000a10m01d-20001001212101">§</a> <a id="2000a10m01d-20001001212101"></a>
  ```
  - a vim shortcut to create a timestamp is `<c-k>ts`
- the sketch drafting and design section has some tips for creating internal cross-references [^1]

------

[^1]: [OpenAI’s new prompting guide: how to get the best results from reasoning models](https://blog.stackademic.com/openais-new-prompting-guide-how-to-get-the-best-results-from-reasoning-models-354a6adf76c2)
