import os

def split_and_rename_data(input_file, output_dir):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = f.read().splitlines()

    count = 1
    w_count = 1
    for i in range(0, len(data), 350):
        output_filename = f"S{count:04d}.txt"
        output_path = os.path.join(output_dir, output_filename)

        with open(output_path, 'w', encoding='utf-8') as out_f:
            for j in range(i, min(i + 350, len(data))):
                audio_name = f"VoiceDataS{count:04d}W{w_count:03d}"
                out_f.write(f"{audio_name} {data[j]}\n")
                w_count += 1

        count += 1
        w_count = 1

    print("Data splitting and renaming completed.")


if __name__ == "__main__":
    input_file = "output.txt"
    output_dir = "output_files"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    split_and_rename_data(input_file, output_dir)