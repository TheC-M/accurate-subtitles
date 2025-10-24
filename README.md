<div align="center" style="margin-bottom: 20px;">

<h1 style="font-size: 2.2em; margin-bottom: 0;">🎯 Accurate Subtitles</h1>
<h3 style="margin-top: 5px; color: #666;">Improving Speech-to-Text Accuracy Through Audio Enhancement, Diarisation, and Context</h3>


</div>


</div>

---

<div align="center">

| <strong>Supervisor:</strong> Dr. Haoyi Wang |
|---------------------------------------------|

<p style="margin: 4px 0; font-style: italic; color: #444;">
  <strong>BSc (Hons) Computer Science</strong><br>
  COMP3000: Computing Project
</p>

</div>


<h3>Project Vision</h3>

  <blockquote style="margin: 10px 0; padding: 10px 14px; background-color: #fff; border-left: 4px solid #0366d6; border-radius: 4px;">
    The aim of this project is to design and implement an AI-driven subtitle generation pipeline that produces highly accurate transcriptions of spoken media, automating most of the process and reducing time spent on manual review and correction. 

While existing speech-to-text (STT) solutions offer strong baseline accuracy, they often lack contextual understanding and speaker identification. This results in errors and a reduction in subtitle quality when handling audio involving multiple speakers - especially with overlapping dialogue - and misinterpretations of technical jargon, names, and domain-specific language. Alongside this improvement, the system will output properly formatted, synchronised, and gramatically correct subtitle (.srt) files, handling challenges like timing, optimised line length, and speaker changes.

The primary audience is accessibility-focused users who depend on subtitles for comprehension, such as those with hearing impairments, auditory processing differences, or limited language proficiency. Secondary users include students and professionals who require accurate and reliable transcripts for documenting lectures and meetings, or for integration into development workflows.

The system will be developed primarily in Python, and will use OpenAI Whisper for the core speech recognition functionality, however the goal is to later experiement with training a new model for comparison and development of skills. The multi-step subtitle generation process will include:

* <strong>Pre-Processing</strong> - Enhance raw audio through noise reduction, speech isolation, and other techniques to  aid transcription accuracy via signal-processing and/or AI-based methods.
* <strong>Speaker Diarisation</strong> - Segment audio and label speakers through use of AI models and/or clustering techniques, potentially handling overlapping speech.
* <strong>Speech-to-Text Transcription</strong> - The audio file(s) will be run through an AI model to generate a timecoded transcript.
* <strong>Post-Processing</strong> - Refine the transcript through context-aware text correction using NLP techniques, alongside the automated and manual gathering of context.
* <strong>Output Formatting</strong> - Produce synchronised, readable and effectively formatted subtitle (.srt) files.
* <strong>Evaluation</strong> - Assess the accuracy of the output using key metrics, alongside flagging sections needing manual review.
  </blockquote>
