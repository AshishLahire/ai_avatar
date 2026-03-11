# script.py
# generates motivational script


def generate_script(title):

    print("\nStep 2: Generating script prompt...")

    prompt = f"Write a short motivational YouTube shorts script for the title: {title}"

    print("Prompt used:")
    print(prompt)

    script = f"""
Most people wait for motivation.

But successful people rely on discipline.

Remember this: {title}.

Small actions repeated every day create massive success.
"""

    print("\nScript generated successfully.")

    return script.strip()