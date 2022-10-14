#!/usr/bin/env python
# coding: utf-8

# # Introduction
# 
# This document is an introduction to Graph-Rewriting Automata and the GRA library.
# 
# ## General concept
# 
# A **Graph-Rewriting Automaton** consists of:
# * an **initial graph** $G_0$ defined at time step $t=0$,
# * a **rule** to iteratively evolve it to any discrete time step $t>0$.
# 
# $G_t$ is the graph obtained at time $t$.
