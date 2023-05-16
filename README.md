# FinNLP_2023
Submission for FinNLP_ESG2023 
Link Share Task --> https://sites.google.com/nlg.csie.ntu.edu.tw/finnlp-2023/shared-task-esg-issue

We are excited to announce the release of the test sets. We kindly request you to refer to the accompanying JSON files attached to this email.

For a smooth submission process, we have set out a few guidelines:

1. Each participating team has the opportunity to submit three system outputs for every language. We would appreciate it if you could follow the given naming format: "<Team Name>_<Language>_<Submission Number>.json". To illustrate, some examples might look like this: FinNLP_English_1.json, FinNLP_French_2.json, and FinNLP_Chinese_3.json.

2. We require you to include the key 'ESG_label' and the predicted label as its corresponding value in your test set JSON file. Here is a model example for your reference:

{
"URL": "https://esgnews.com/los-angeles-unified-and-att-deliver-high-speed-internet-to-students-homes-to-bridge-the-digital-divide/",
"news_title": "Broadband with Speeds Up to 1 GIG is Provided at No Cost to Families Through the FCC\u2019s Emergency Connectivity Fund",
"news_content": "What\u2019s the news? Los Angeles Unified School District and AT&T* are providing high-speed broadband to students\u2019 homes at no cost to their families. As we reimagine the future of education, connectivity is the new pen and paper. And through this joint effort, more students and households in Los Angeles will have the reliable internet needed to fully participate in education and digital life.",
"ESG_label": "PREDICTED VALUE HERE"
}

3. Submissions should be emailed to <finnlp@nlg.csie.ntu.edu.tw> no later than May 22, 2023 (AoE). For the subject line of your email, please use "<Team Name> ML-ESG Submissions."
