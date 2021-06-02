# The-Level-of-Communication
Have you ever wonder when reading a job posting online, we can identify the all of the skill. But how about the level ? 

For example, when a job description said: 
> _"Require a Good Communication Skill"_

What do they mean about that ? What is _a Good Communication_ and how can we define it ?

The method that I'm using is __Natural Language Processing (NLP)__ combine with __Decision Tree__ to identify the level of communication in a job posting

## Idea
The project is inspired by the __Centre of Change and Complexity (C3L)__ where I take the internship and __Dr. Jing Gao__ as the supervisor.

## Methodology
We will extract information from the job posting and use it as a criteria to split down the tree until we can identify the level of communication

This would include: __Job Levels, Job Categories, Job Skills and Communication Asessment Score (IELTS)__

### Procedure
  1. Preprocessing Job Posting
  2. Classify the __Job Levels__ base on the __Job Title__
  3. Classify the __Categories__ base on the __Job Description__
  4. Using the __Job Description__ to identify all of the skill
  5. Getting __University Entry Requirement IELTS__ and use that for the __Entry Level__ (which is __normal communication skill__) 
  6. And then base on the two __Job Level and Categories__ with the inference from the __Communication Asessment Score__ to return a final result -> Kind of like an ensemble model where it combine multi minor model to finalize an outcome

## Outcome
Web-App Dashboard: [Communication Level](https://communication-level.herokuapp.com)
