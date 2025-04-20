import requests

def get_all_breeds():
    try:
        response = requests.get("https://dog.ceo/api/breeds/list/all")
        response.raise_for_status()
        data = response.json()
        return data["message"]
    except requests.exceptions.RequestException:
        print("Error: Could not fetch breed list from API.")
        return {}

def get_random_image(breed):
    try:
        response = requests.get(f"https://dog.ceo/api/breed/{breed}/images/random")
        response.raise_for_status()
        data = response.json()
        return data["message"]
    except requests.exceptions.RequestException:
        print(f"Error: Could not fetch image for breed '{breed}'.")
        return None

def get_random_sub_breed_image(breed, sub_breed):
    try:                
        response = requests.get(f"https://dog.ceo/api/breed/{breed}/{sub_breed}/images/random")
        response.raise_for_status()
        data = response.json()
        return data["message"]
    except requests.exceptions.RequestException:
        print(f"Error: Could not fetch image for sub-breed '{sub_breed}' of breed '{breed}'.")
        return None

def show_breeds(breeds_dict):
    sorted_breeds = sorted(breeds_dict.keys())
    for i in range(0, len(sorted_breeds), 5):
        print(", ".join(sorted_breeds[i:i+5]))

def main():
    while True:
        print("\nWhat would you like to do?")
        print("1. Show all breeds")
        print("2. Get a random image from a breed")
        print("3. Get a random image from a sub-breed")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        try:
            if choice == "1":
                breeds = get_all_breeds()
                show_breeds(breeds)

            elif choice == "2":
                breeds = get_all_breeds()
                breed = input("Enter breed name: ").strip().lower()
                if breed in breeds:
                    image_url = get_random_image(breed)
                    if image_url:
                        print(f"Random image URL for {breed}: {image_url}")
                else:
                    print("Invalid breed name. Please try again.")

            elif choice == "3":
                breeds = get_all_breeds()
                breed = input("Enter breed name: ").strip().lower()
                if breed in breeds and breeds[breed]:
                    print("Available sub-breeds:", ", ".join(breeds[breed]))
                    sub_breed = input("Enter sub-breed name: ").strip().lower()
                    if sub_breed in breeds[breed]:
                        image_url = get_random_sub_breed_image(breed, sub_breed)
                        if image_url:
                            print(f"Random image URL for {sub_breed} {breed}: {image_url}")
                    else:
                        print("Invalid sub-breed name. Please try again.")
                else:
                    print("Either invalid breed or no sub-breeds available for this breed.")

            elif choice == "4":
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please select a number between 1 and 4.")

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
