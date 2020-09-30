# raspberry_pc_switch
remotely turn on and off pc, using a raspberry

Allow access to raspberry pins: 
```
sudo chown root.gpio /dev/gpiomem
sudo chmod g+rw /dev/gpiomem
```

TURN OFF (should turn off with 4-6 seconds): 
```python set_gpio_to_true_for_a_while.py --duration=6```

TURN ON (usually shorter duration for turning on the machine):
```python set_gpio_to_true_for_a_while.py --duration=2```


