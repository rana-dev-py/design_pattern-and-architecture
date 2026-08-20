"""Python callbacks are a lightweight observer mechanism."""
listeners = []
def on_change(callback): listeners.append(callback)
def set_value(value):
    for listener in listeners: listener(value)

on_change(print); set_value("updated")
