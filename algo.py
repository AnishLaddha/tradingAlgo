{\rtf1\ansi\ansicpg1252\cocoartf1561\cocoasubrtf400
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 def initialize(context):\
    context.gld = sid(26807)\
    context.faang = sid(36376)\
    schedule_function(ma_crossover_handling_gld, date_rules.every_day(), time_rules.market_open())\
    schedule_function(ma_crossover_handling_faang, date_rules.every_day(), time_rules.market_open())\
   \
def ma_crossover_handling_gld(context, data):\
    histgld = data.history(context.gld, 'price', 30, '1d')\
    \
    sma_30 = histgld.mean()\
    sma_15 = histgld[-15:].mean()\
    \
    open_orders = get_open_orders()\
    \
    if sma_15 > sma_30:\
        if context.gld not in open_orders:\
            order_target_percent(context.gld, -0.5)\
    elif sma_15< sma_30:\
        if context.gld not in open_orders:\
            order_target_percent(context.gld, 0.5)\
    \
    record(leverage = context.account.leverage)\
def ma_crossover_handling_faang(context, data):\
    histfaang = data.history(context.faang, 'price', 20, '1d')\
    sma_20 = histfaang.mean()\
    sma_10 = histfaang[-10:].mean()\
    open_orders = get_open_orders()\
    if sma_10>sma_20:\
        if context.faang not in open_orders:\
            order_target_percent(context.faang, 0.5)\
    if sma_10<sma_20:\
        if context.faang not in open_orders:\
            order_target_percent(context.faang, -0.5)}