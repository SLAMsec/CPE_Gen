def generate_cpe():
    # Collecting information from the user
    part = input("Enter the part (e.g., 'a' for application, 'o' for operating system, 'h' for hardware): ")
    vendor = input("Enter the vendor name: ")
    product = input("Enter the product name: ")
    version = input("Enter the version: ")
    update = input("Enter the update (if any): ")
    edition = input("Enter the edition (if any): ")
    language = input("Enter the language (if any): ")

    # Constructing the CPE string
    cpe = f"cpe:2.3:{part}:{vendor}:{product}:{version}:{update}:{edition}::{language}"

    return cpe

# Generate and print the CPE
cpe_string = generate_cpe()
print(f"The generated CPE is: {cpe_string}")
