#!/bin/bash
screen -d -m -S leddie sh backend.sh & screen -d -m -S website sh backend.sh
