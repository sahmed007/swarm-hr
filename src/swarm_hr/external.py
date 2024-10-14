from openai import OpenAI


def assess_candidate_fit(candidate_skills: list, job_position: str) -> bool:
    client = OpenAI()

    prompt = (
        f"Given the following candidate skills: {', '.join(candidate_skills)}, "
        f"assess if they are a good fit for the position of {job_position}. "
        f"Respond with 'Yes' if they are a good fit, or 'No' if they are not. "
        f"Provide a detailed 2-3 sentence explanation for your assessment."
    )

    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You are an HR assistant evaluating candidate fit.",
            },
            {"role": "user", "content": prompt},
        ],
        max_tokens=100,
        n=1,
        temperature=0.5,
    )

    answer = completion.choices[0].message.content.strip().lower()
    return answer
