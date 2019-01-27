#!/bin/sh
@echo off
echo ====== Smoking ======
echo ====== Test Show ======
books
echo ====== Test Add ======
books add "Hello, world" 500
books show
echo ====== Test Read ======
books --read 10013 128
books -r 11111 11
books 10001 8888888
books -s
echo ====== Test Delete ======
books -d 10013
books --show
echo ====== No Smoking ======
