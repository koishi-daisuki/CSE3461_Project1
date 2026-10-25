# Feature 3 - Reliable UDP chat under simulated packet loss
This working standalone F3 prototype extends communication behavior using
application-layer acknowledgments, stop-and-wait retransmission, and duplicate
suppression. It includes a terminal chat and a reproducible comparison against
send-once UDP. The main chat application requires only Python's standard library. The Matplotlib is required for figure for demonstrating purpose.

## Run the chat
Terminal A:

```sh
python3 chat.py --port 5000 --peer-port 5001 --loss .2
```

Terminal B:

```sh
python3 chat.py --port 5001 --peer-port 5000 --loss .2
```

## Run the benchmark and simulation

```sh
python3 benchmark.py
python3 -m unittest -v test_f3
```

```sh
python3 plot_results.py --results-dir results

