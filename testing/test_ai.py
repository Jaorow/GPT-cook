import openai
import argparse

import os
# openai.organization = "org"
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_recipe(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()

def main():
    parser = argparse.ArgumentParser(description='Generate recipe recommendations for a student to cook throught the week')
    parser.add_argument('--prompt', type=str, help='Prompt for generating recipe recommendations', required=True)

    args = parser.parse_args()

    recipe = generate_recipe(args.prompt)

    print(recipe)

if __name__ == '__main__':
    main()
