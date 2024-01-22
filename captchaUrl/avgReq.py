def calculate_avg_requests(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    total_requests = 0
    unique_links = set()

    for line in lines:
        link, count = line.strip().split(" | ")
        total_requests += 1
        unique_links.add(link)

        if len(unique_links) != total_requests:
            break

    avg_requests = total_requests / len(unique_links)
    return avg_requests

file_path = "url_counts_threaded.txt"
avg_requests = calculate_avg_requests(file_path)

print(f"Average number of requests till duplicate link: {avg_requests}")
