# CodeAlpha_NETWORK_SNIFFER

# Network Scanner

A simple Python-based network scanner using Scapy to discover devices in a specified IP range or network. This tool sends ARP requests to identify active hosts and their corresponding MAC addresses on the network.

## Features

- Scans a specified IP address or network range to identify active devices.
- Displays the IP address and MAC address of discovered devices.
- Verbose mode for detailed output.

## Prerequisites

- Python 3.x
- Scapy library

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/network-scanner.git
    cd network-scanner
    ```

2. **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the network scanner with the desired options.

### Options

- `-r`, `--range`: Specify the IP address or network range to scan (required).
- `-v`, `--verbose`: Enable verbose output (optional).

### Example

To scan a network range:

```bash
python network_scanner.py -r 192.168.1.1/24
```

To scan a single IP address with verbose output:

```bash
python network_scanner.py -r 192.168.1.1 -v
```

### Output

The script will display the list of active devices in the specified network range with their IP and MAC addresses.

```
IP Address          MAC Address
------------------------------------------
192.168.1.2         00:1A:2B:3C:4D:5E
192.168.1.3         00:1A:2B:3C:4D:5F
...
```

## Error Handling

If an invalid IP address or network range is specified, the script will display an error message and exit.

```
[-] Please specify a valid IP Address or Network Range
```

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Scapy](https://scapy.net/) - The powerful Python-based interactive packet manipulation program used in this project.
