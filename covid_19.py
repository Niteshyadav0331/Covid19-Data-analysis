{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Importing important libraries"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [],
   "source": [
    "%matplotlib inline\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Province/State</th>\n",
       "      <th>Country/Region</th>\n",
       "      <th>Lat</th>\n",
       "      <th>Long</th>\n",
       "      <th>1/22/20</th>\n",
       "      <th>1/23/20</th>\n",
       "      <th>1/24/20</th>\n",
       "      <th>1/25/20</th>\n",
       "      <th>1/26/20</th>\n",
       "      <th>1/27/20</th>\n",
       "      <th>...</th>\n",
       "      <th>6/12/20</th>\n",
       "      <th>6/13/20</th>\n",
       "      <th>6/14/20</th>\n",
       "      <th>6/15/20</th>\n",
       "      <th>6/16/20</th>\n",
       "      <th>6/17/20</th>\n",
       "      <th>6/18/20</th>\n",
       "      <th>6/19/20</th>\n",
       "      <th>6/20/20</th>\n",
       "      <th>6/21/20</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>NaN</td>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>33.0000</td>\n",
       "      <td>65.0000</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>23546</td>\n",
       "      <td>24102</td>\n",
       "      <td>24766</td>\n",
       "      <td>25527</td>\n",
       "      <td>26310</td>\n",
       "      <td>26874</td>\n",
       "      <td>27532</td>\n",
       "      <td>27878</td>\n",
       "      <td>28424</td>\n",
       "      <td>28833</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>NaN</td>\n",
       "      <td>Albania</td>\n",
       "      <td>41.1533</td>\n",
       "      <td>20.1683</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1416</td>\n",
       "      <td>1464</td>\n",
       "      <td>1521</td>\n",
       "      <td>1590</td>\n",
       "      <td>1672</td>\n",
       "      <td>1722</td>\n",
       "      <td>1788</td>\n",
       "      <td>1838</td>\n",
       "      <td>1891</td>\n",
       "      <td>1962</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>NaN</td>\n",
       "      <td>Algeria</td>\n",
       "      <td>28.0339</td>\n",
       "      <td>1.6596</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>10698</td>\n",
       "      <td>10810</td>\n",
       "      <td>10919</td>\n",
       "      <td>11031</td>\n",
       "      <td>11147</td>\n",
       "      <td>11268</td>\n",
       "      <td>11385</td>\n",
       "      <td>11504</td>\n",
       "      <td>11631</td>\n",
       "      <td>11771</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>NaN</td>\n",
       "      <td>Andorra</td>\n",
       "      <td>42.5063</td>\n",
       "      <td>1.5218</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>853</td>\n",
       "      <td>853</td>\n",
       "      <td>853</td>\n",
       "      <td>853</td>\n",
       "      <td>854</td>\n",
       "      <td>854</td>\n",
       "      <td>855</td>\n",
       "      <td>855</td>\n",
       "      <td>855</td>\n",
       "      <td>855</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>NaN</td>\n",
       "      <td>Angola</td>\n",
       "      <td>-11.2027</td>\n",
       "      <td>17.8739</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>130</td>\n",
       "      <td>138</td>\n",
       "      <td>140</td>\n",
       "      <td>142</td>\n",
       "      <td>148</td>\n",
       "      <td>155</td>\n",
       "      <td>166</td>\n",
       "      <td>172</td>\n",
       "      <td>176</td>\n",
       "      <td>183</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 156 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "  Province/State Country/Region      Lat     Long  1/22/20  1/23/20  1/24/20  \\\n",
       "0            NaN    Afghanistan  33.0000  65.0000        0        0        0   \n",
       "1            NaN        Albania  41.1533  20.1683        0        0        0   \n",
       "2            NaN        Algeria  28.0339   1.6596        0        0        0   \n",
       "3            NaN        Andorra  42.5063   1.5218        0        0        0   \n",
       "4            NaN         Angola -11.2027  17.8739        0        0        0   \n",
       "\n",
       "   1/25/20  1/26/20  1/27/20  ...  6/12/20  6/13/20  6/14/20  6/15/20  \\\n",
       "0        0        0        0  ...    23546    24102    24766    25527   \n",
       "1        0        0        0  ...     1416     1464     1521     1590   \n",
       "2        0        0        0  ...    10698    10810    10919    11031   \n",
       "3        0        0        0  ...      853      853      853      853   \n",
       "4        0        0        0  ...      130      138      140      142   \n",
       "\n",
       "   6/16/20  6/17/20  6/18/20  6/19/20  6/20/20  6/21/20  \n",
       "0    26310    26874    27532    27878    28424    28833  \n",
       "1     1672     1722     1788     1838     1891     1962  \n",
       "2    11147    11268    11385    11504    11631    11771  \n",
       "3      854      854      855      855      855      855  \n",
       "4      148      155      166      172      176      183  \n",
       "\n",
       "[5 rows x 156 columns]"
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Importing data \n",
    "df = pd.read_csv(\"time_series_covid19_confirmed_global.csv\")\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [],
   "source": [
    "#dropping unnecessary cols\n",
    "\n",
    "df.drop([\"Lat\", \"Long\"], axis = 1, inplace = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Province/State</th>\n",
       "      <th>Country/Region</th>\n",
       "      <th>1/22/20</th>\n",
       "      <th>1/23/20</th>\n",
       "      <th>1/24/20</th>\n",
       "      <th>1/25/20</th>\n",
       "      <th>1/26/20</th>\n",
       "      <th>1/27/20</th>\n",
       "      <th>1/28/20</th>\n",
       "      <th>1/29/20</th>\n",
       "      <th>...</th>\n",
       "      <th>6/12/20</th>\n",
       "      <th>6/13/20</th>\n",
       "      <th>6/14/20</th>\n",
       "      <th>6/15/20</th>\n",
       "      <th>6/16/20</th>\n",
       "      <th>6/17/20</th>\n",
       "      <th>6/18/20</th>\n",
       "      <th>6/19/20</th>\n",
       "      <th>6/20/20</th>\n",
       "      <th>6/21/20</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>NaN</td>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>23546</td>\n",
       "      <td>24102</td>\n",
       "      <td>24766</td>\n",
       "      <td>25527</td>\n",
       "      <td>26310</td>\n",
       "      <td>26874</td>\n",
       "      <td>27532</td>\n",
       "      <td>27878</td>\n",
       "      <td>28424</td>\n",
       "      <td>28833</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>NaN</td>\n",
       "      <td>Albania</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1416</td>\n",
       "      <td>1464</td>\n",
       "      <td>1521</td>\n",
       "      <td>1590</td>\n",
       "      <td>1672</td>\n",
       "      <td>1722</td>\n",
       "      <td>1788</td>\n",
       "      <td>1838</td>\n",
       "      <td>1891</td>\n",
       "      <td>1962</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>NaN</td>\n",
       "      <td>Algeria</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>10698</td>\n",
       "      <td>10810</td>\n",
       "      <td>10919</td>\n",
       "      <td>11031</td>\n",
       "      <td>11147</td>\n",
       "      <td>11268</td>\n",
       "      <td>11385</td>\n",
       "      <td>11504</td>\n",
       "      <td>11631</td>\n",
       "      <td>11771</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>NaN</td>\n",
       "      <td>Andorra</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>853</td>\n",
       "      <td>853</td>\n",
       "      <td>853</td>\n",
       "      <td>853</td>\n",
       "      <td>854</td>\n",
       "      <td>854</td>\n",
       "      <td>855</td>\n",
       "      <td>855</td>\n",
       "      <td>855</td>\n",
       "      <td>855</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>NaN</td>\n",
       "      <td>Angola</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>130</td>\n",
       "      <td>138</td>\n",
       "      <td>140</td>\n",
       "      <td>142</td>\n",
       "      <td>148</td>\n",
       "      <td>155</td>\n",
       "      <td>166</td>\n",
       "      <td>172</td>\n",
       "      <td>176</td>\n",
       "      <td>183</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 154 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "  Province/State Country/Region  1/22/20  1/23/20  1/24/20  1/25/20  1/26/20  \\\n",
       "0            NaN    Afghanistan        0        0        0        0        0   \n",
       "1            NaN        Albania        0        0        0        0        0   \n",
       "2            NaN        Algeria        0        0        0        0        0   \n",
       "3            NaN        Andorra        0        0        0        0        0   \n",
       "4            NaN         Angola        0        0        0        0        0   \n",
       "\n",
       "   1/27/20  1/28/20  1/29/20  ...  6/12/20  6/13/20  6/14/20  6/15/20  \\\n",
       "0        0        0        0  ...    23546    24102    24766    25527   \n",
       "1        0        0        0  ...     1416     1464     1521     1590   \n",
       "2        0        0        0  ...    10698    10810    10919    11031   \n",
       "3        0        0        0  ...      853      853      853      853   \n",
       "4        0        0        0  ...      130      138      140      142   \n",
       "\n",
       "   6/16/20  6/17/20  6/18/20  6/19/20  6/20/20  6/21/20  \n",
       "0    26310    26874    27532    27878    28424    28833  \n",
       "1     1672     1722     1788     1838     1891     1962  \n",
       "2    11147    11268    11385    11504    11631    11771  \n",
       "3      854      854      855      855      855      855  \n",
       "4      148      155      166      172      176      183  \n",
       "\n",
       "[5 rows x 154 columns]"
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Aggregating by country name"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_agg = df.groupby(\"Country/Region\").sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>1/22/20</th>\n",
       "      <th>1/23/20</th>\n",
       "      <th>1/24/20</th>\n",
       "      <th>1/25/20</th>\n",
       "      <th>1/26/20</th>\n",
       "      <th>1/27/20</th>\n",
       "      <th>1/28/20</th>\n",
       "      <th>1/29/20</th>\n",
       "      <th>1/30/20</th>\n",
       "      <th>1/31/20</th>\n",
       "      <th>...</th>\n",
       "      <th>6/12/20</th>\n",
       "      <th>6/13/20</th>\n",
       "      <th>6/14/20</th>\n",
       "      <th>6/15/20</th>\n",
       "      <th>6/16/20</th>\n",
       "      <th>6/17/20</th>\n",
       "      <th>6/18/20</th>\n",
       "      <th>6/19/20</th>\n",
       "      <th>6/20/20</th>\n",
       "      <th>6/21/20</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Country/Region</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Afghanistan</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>23546</td>\n",
       "      <td>24102</td>\n",
       "      <td>24766</td>\n",
       "      <td>25527</td>\n",
       "      <td>26310</td>\n",
       "      <td>26874</td>\n",
       "      <td>27532</td>\n",
       "      <td>27878</td>\n",
       "      <td>28424</td>\n",
       "      <td>28833</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Albania</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1416</td>\n",
       "      <td>1464</td>\n",
       "      <td>1521</td>\n",
       "      <td>1590</td>\n",
       "      <td>1672</td>\n",
       "      <td>1722</td>\n",
       "      <td>1788</td>\n",
       "      <td>1838</td>\n",
       "      <td>1891</td>\n",
       "      <td>1962</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Algeria</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>10698</td>\n",
       "      <td>10810</td>\n",
       "      <td>10919</td>\n",
       "      <td>11031</td>\n",
       "      <td>11147</td>\n",
       "      <td>11268</td>\n",
       "      <td>11385</td>\n",
       "      <td>11504</td>\n",
       "      <td>11631</td>\n",
       "      <td>11771</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Andorra</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>853</td>\n",
       "      <td>853</td>\n",
       "      <td>853</td>\n",
       "      <td>853</td>\n",
       "      <td>854</td>\n",
       "      <td>854</td>\n",
       "      <td>855</td>\n",
       "      <td>855</td>\n",
       "      <td>855</td>\n",
       "      <td>855</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Angola</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>130</td>\n",
       "      <td>138</td>\n",
       "      <td>140</td>\n",
       "      <td>142</td>\n",
       "      <td>148</td>\n",
       "      <td>155</td>\n",
       "      <td>166</td>\n",
       "      <td>172</td>\n",
       "      <td>176</td>\n",
       "      <td>183</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 152 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                1/22/20  1/23/20  1/24/20  1/25/20  1/26/20  1/27/20  1/28/20  \\\n",
       "Country/Region                                                                  \n",
       "Afghanistan           0        0        0        0        0        0        0   \n",
       "Albania               0        0        0        0        0        0        0   \n",
       "Algeria               0        0        0        0        0        0        0   \n",
       "Andorra               0        0        0        0        0        0        0   \n",
       "Angola                0        0        0        0        0        0        0   \n",
       "\n",
       "                1/29/20  1/30/20  1/31/20  ...  6/12/20  6/13/20  6/14/20  \\\n",
       "Country/Region                             ...                              \n",
       "Afghanistan           0        0        0  ...    23546    24102    24766   \n",
       "Albania               0        0        0  ...     1416     1464     1521   \n",
       "Algeria               0        0        0  ...    10698    10810    10919   \n",
       "Andorra               0        0        0  ...      853      853      853   \n",
       "Angola                0        0        0  ...      130      138      140   \n",
       "\n",
       "                6/15/20  6/16/20  6/17/20  6/18/20  6/19/20  6/20/20  6/21/20  \n",
       "Country/Region                                                                 \n",
       "Afghanistan       25527    26310    26874    27532    27878    28424    28833  \n",
       "Albania            1590     1672     1722     1788     1838     1891     1962  \n",
       "Algeria           11031    11147    11268    11385    11504    11631    11771  \n",
       "Andorra             853      854      854      855      855      855      855  \n",
       "Angola              142      148      155      166      172      176      183  \n",
       "\n",
       "[5 rows x 152 columns]"
      ]
     },
     "execution_count": 87,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_agg.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Visualizing the confirmed cases yill 06/10/2020 (mm/dd/yyyy)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.legend.Legend at 0x1edf086c588>"
      ]
     },
     "execution_count": 88,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df_agg.loc['China'].plot()\n",
    "df_agg.loc['India'].plot()\n",
    "df_agg.loc['Italy'].plot()\n",
    "plt.legend()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## visualizing data according to dates"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.legend.Legend at 0x1edf0b1a808>"
      ]
     },
     "execution_count": 89,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1800x720 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize = (25, 10))\n",
    "df_agg.loc[\"China\"][:30].plot()\n",
    "df_agg.loc[\"India\"][:30].plot()\n",
    "plt.legend()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## To check the new confirmed cases we need to find the first derivative by using diff() func "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.legend.Legend at 0x1edf1928a88>"
      ]
     },
     "execution_count": 90,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df_agg.loc[\"China\"].diff().plot()\n",
    "df_agg.loc[\"India\"].diff().plot()\n",
    "plt.legend()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "15136.0"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Maximum infection rate in china in one day\n",
    "df_agg.loc[\"China\"].diff().max()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "15403.0"
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Maximum infection in India in one day\n",
    "df_agg.loc[\"India\"].diff().max()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Finding the max infection rate for all countries and putting in dataset."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {},
   "outputs": [],
   "source": [
    "countries = list(df_agg.index)\n",
    "max_rate = []\n",
    "for i in countries:\n",
    "    max_rate.append(df_agg.loc[i].diff().max())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_agg[\"max_infect_rate\"] = max_rate"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>1/22/20</th>\n",
       "      <th>1/23/20</th>\n",
       "      <th>1/24/20</th>\n",
       "      <th>1/25/20</th>\n",
       "      <th>1/26/20</th>\n",
       "      <th>1/27/20</th>\n",
       "      <th>1/28/20</th>\n",
       "      <th>1/29/20</th>\n",
       "      <th>1/30/20</th>\n",
       "      <th>1/31/20</th>\n",
       "      <th>...</th>\n",
       "      <th>6/13/20</th>\n",
       "      <th>6/14/20</th>\n",
       "      <th>6/15/20</th>\n",
       "      <th>6/16/20</th>\n",
       "      <th>6/17/20</th>\n",
       "      <th>6/18/20</th>\n",
       "      <th>6/19/20</th>\n",
       "      <th>6/20/20</th>\n",
       "      <th>6/21/20</th>\n",
       "      <th>max_infect_rate</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Country/Region</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Afghanistan</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>24102</td>\n",
       "      <td>24766</td>\n",
       "      <td>25527</td>\n",
       "      <td>26310</td>\n",
       "      <td>26874</td>\n",
       "      <td>27532</td>\n",
       "      <td>27878</td>\n",
       "      <td>28424</td>\n",
       "      <td>28833</td>\n",
       "      <td>915.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Albania</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1464</td>\n",
       "      <td>1521</td>\n",
       "      <td>1590</td>\n",
       "      <td>1672</td>\n",
       "      <td>1722</td>\n",
       "      <td>1788</td>\n",
       "      <td>1838</td>\n",
       "      <td>1891</td>\n",
       "      <td>1962</td>\n",
       "      <td>82.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Algeria</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>10810</td>\n",
       "      <td>10919</td>\n",
       "      <td>11031</td>\n",
       "      <td>11147</td>\n",
       "      <td>11268</td>\n",
       "      <td>11385</td>\n",
       "      <td>11504</td>\n",
       "      <td>11631</td>\n",
       "      <td>11771</td>\n",
       "      <td>199.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Andorra</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>853</td>\n",
       "      <td>853</td>\n",
       "      <td>853</td>\n",
       "      <td>854</td>\n",
       "      <td>854</td>\n",
       "      <td>855</td>\n",
       "      <td>855</td>\n",
       "      <td>855</td>\n",
       "      <td>855</td>\n",
       "      <td>79.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Angola</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>138</td>\n",
       "      <td>140</td>\n",
       "      <td>142</td>\n",
       "      <td>148</td>\n",
       "      <td>155</td>\n",
       "      <td>166</td>\n",
       "      <td>172</td>\n",
       "      <td>176</td>\n",
       "      <td>183</td>\n",
       "      <td>17.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 153 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                1/22/20  1/23/20  1/24/20  1/25/20  1/26/20  1/27/20  1/28/20  \\\n",
       "Country/Region                                                                  \n",
       "Afghanistan           0        0        0        0        0        0        0   \n",
       "Albania               0        0        0        0        0        0        0   \n",
       "Algeria               0        0        0        0        0        0        0   \n",
       "Andorra               0        0        0        0        0        0        0   \n",
       "Angola                0        0        0        0        0        0        0   \n",
       "\n",
       "                1/29/20  1/30/20  1/31/20  ...  6/13/20  6/14/20  6/15/20  \\\n",
       "Country/Region                             ...                              \n",
       "Afghanistan           0        0        0  ...    24102    24766    25527   \n",
       "Albania               0        0        0  ...     1464     1521     1590   \n",
       "Algeria               0        0        0  ...    10810    10919    11031   \n",
       "Andorra               0        0        0  ...      853      853      853   \n",
       "Angola                0        0        0  ...      138      140      142   \n",
       "\n",
       "                6/16/20  6/17/20  6/18/20  6/19/20  6/20/20  6/21/20  \\\n",
       "Country/Region                                                         \n",
       "Afghanistan       26310    26874    27532    27878    28424    28833   \n",
       "Albania            1672     1722     1788     1838     1891     1962   \n",
       "Algeria           11147    11268    11385    11504    11631    11771   \n",
       "Andorra             854      854      855      855      855      855   \n",
       "Angola              148      155      166      172      176      183   \n",
       "\n",
       "                max_infect_rate  \n",
       "Country/Region                   \n",
       "Afghanistan               915.0  \n",
       "Albania                    82.0  \n",
       "Algeria                   199.0  \n",
       "Andorra                    79.0  \n",
       "Angola                     17.0  \n",
       "\n",
       "[5 rows x 153 columns]"
      ]
     },
     "execution_count": 95,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_agg.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {},
   "outputs": [],
   "source": [
    "corona_data = pd.DataFrame(df_agg[\"max_infect_rate\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>max_infect_rate</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Country/Region</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Afghanistan</th>\n",
       "      <td>915.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Albania</th>\n",
       "      <td>82.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Algeria</th>\n",
       "      <td>199.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Andorra</th>\n",
       "      <td>79.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Angola</th>\n",
       "      <td>17.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                max_infect_rate\n",
       "Country/Region                 \n",
       "Afghanistan               915.0\n",
       "Albania                    82.0\n",
       "Algeria                   199.0\n",
       "Andorra                    79.0\n",
       "Angola                     17.0"
      ]
     },
     "execution_count": 97,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "corona_data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(188, 1)"
      ]
     },
     "execution_count": 98,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "corona_data.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Overall rank</th>\n",
       "      <th>Country or region</th>\n",
       "      <th>Score</th>\n",
       "      <th>GDP per capita</th>\n",
       "      <th>Social support</th>\n",
       "      <th>Healthy life expectancy</th>\n",
       "      <th>Freedom to make life choices</th>\n",
       "      <th>Generosity</th>\n",
       "      <th>Perceptions of corruption</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Finland</td>\n",
       "      <td>7.769</td>\n",
       "      <td>1.340</td>\n",
       "      <td>1.587</td>\n",
       "      <td>0.986</td>\n",
       "      <td>0.596</td>\n",
       "      <td>0.153</td>\n",
       "      <td>0.393</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>Denmark</td>\n",
       "      <td>7.600</td>\n",
       "      <td>1.383</td>\n",
       "      <td>1.573</td>\n",
       "      <td>0.996</td>\n",
       "      <td>0.592</td>\n",
       "      <td>0.252</td>\n",
       "      <td>0.410</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>Norway</td>\n",
       "      <td>7.554</td>\n",
       "      <td>1.488</td>\n",
       "      <td>1.582</td>\n",
       "      <td>1.028</td>\n",
       "      <td>0.603</td>\n",
       "      <td>0.271</td>\n",
       "      <td>0.341</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>Iceland</td>\n",
       "      <td>7.494</td>\n",
       "      <td>1.380</td>\n",
       "      <td>1.624</td>\n",
       "      <td>1.026</td>\n",
       "      <td>0.591</td>\n",
       "      <td>0.354</td>\n",
       "      <td>0.118</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>Netherlands</td>\n",
       "      <td>7.488</td>\n",
       "      <td>1.396</td>\n",
       "      <td>1.522</td>\n",
       "      <td>0.999</td>\n",
       "      <td>0.557</td>\n",
       "      <td>0.322</td>\n",
       "      <td>0.298</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Overall rank Country or region  Score  GDP per capita  Social support  \\\n",
       "0             1           Finland  7.769           1.340           1.587   \n",
       "1             2           Denmark  7.600           1.383           1.573   \n",
       "2             3            Norway  7.554           1.488           1.582   \n",
       "3             4           Iceland  7.494           1.380           1.624   \n",
       "4             5       Netherlands  7.488           1.396           1.522   \n",
       "\n",
       "   Healthy life expectancy  Freedom to make life choices  Generosity  \\\n",
       "0                    0.986                         0.596       0.153   \n",
       "1                    0.996                         0.592       0.252   \n",
       "2                    1.028                         0.603       0.271   \n",
       "3                    1.026                         0.591       0.354   \n",
       "4                    0.999                         0.557       0.322   \n",
       "\n",
       "   Perceptions of corruption  \n",
       "0                      0.393  \n",
       "1                      0.410  \n",
       "2                      0.341  \n",
       "3                      0.118  \n",
       "4                      0.298  "
      ]
     },
     "execution_count": 99,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_hrep = pd.read_csv(\"worldwide_happiness_report.csv\")\n",
    "df_hrep.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Deleting useless columns \n",
    "useless_cols = [\"Overall rank\",\"Score\",\"Generosity\",\"Perceptions of corruption\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Country or region</th>\n",
       "      <th>GDP per capita</th>\n",
       "      <th>Social support</th>\n",
       "      <th>Healthy life expectancy</th>\n",
       "      <th>Freedom to make life choices</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Finland</td>\n",
       "      <td>1.340</td>\n",
       "      <td>1.587</td>\n",
       "      <td>0.986</td>\n",
       "      <td>0.596</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Denmark</td>\n",
       "      <td>1.383</td>\n",
       "      <td>1.573</td>\n",
       "      <td>0.996</td>\n",
       "      <td>0.592</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Norway</td>\n",
       "      <td>1.488</td>\n",
       "      <td>1.582</td>\n",
       "      <td>1.028</td>\n",
       "      <td>0.603</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Iceland</td>\n",
       "      <td>1.380</td>\n",
       "      <td>1.624</td>\n",
       "      <td>1.026</td>\n",
       "      <td>0.591</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Netherlands</td>\n",
       "      <td>1.396</td>\n",
       "      <td>1.522</td>\n",
       "      <td>0.999</td>\n",
       "      <td>0.557</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Country or region  GDP per capita  Social support  Healthy life expectancy  \\\n",
       "0           Finland           1.340           1.587                    0.986   \n",
       "1           Denmark           1.383           1.573                    0.996   \n",
       "2            Norway           1.488           1.582                    1.028   \n",
       "3           Iceland           1.380           1.624                    1.026   \n",
       "4       Netherlands           1.396           1.522                    0.999   \n",
       "\n",
       "   Freedom to make life choices  \n",
       "0                         0.596  \n",
       "1                         0.592  \n",
       "2                         0.603  \n",
       "3                         0.591  \n",
       "4                         0.557  "
      ]
     },
     "execution_count": 101,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_hrep.drop(useless_cols, axis = 1, inplace = True)\n",
    "df_hrep.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>GDP per capita</th>\n",
       "      <th>Social support</th>\n",
       "      <th>Healthy life expectancy</th>\n",
       "      <th>Freedom to make life choices</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Country or region</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Finland</th>\n",
       "      <td>1.340</td>\n",
       "      <td>1.587</td>\n",
       "      <td>0.986</td>\n",
       "      <td>0.596</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Denmark</th>\n",
       "      <td>1.383</td>\n",
       "      <td>1.573</td>\n",
       "      <td>0.996</td>\n",
       "      <td>0.592</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Norway</th>\n",
       "      <td>1.488</td>\n",
       "      <td>1.582</td>\n",
       "      <td>1.028</td>\n",
       "      <td>0.603</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Iceland</th>\n",
       "      <td>1.380</td>\n",
       "      <td>1.624</td>\n",
       "      <td>1.026</td>\n",
       "      <td>0.591</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Netherlands</th>\n",
       "      <td>1.396</td>\n",
       "      <td>1.522</td>\n",
       "      <td>0.999</td>\n",
       "      <td>0.557</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   GDP per capita  Social support  Healthy life expectancy  \\\n",
       "Country or region                                                            \n",
       "Finland                     1.340           1.587                    0.986   \n",
       "Denmark                     1.383           1.573                    0.996   \n",
       "Norway                      1.488           1.582                    1.028   \n",
       "Iceland                     1.380           1.624                    1.026   \n",
       "Netherlands                 1.396           1.522                    0.999   \n",
       "\n",
       "                   Freedom to make life choices  \n",
       "Country or region                                \n",
       "Finland                                   0.596  \n",
       "Denmark                                   0.592  \n",
       "Norway                                    0.603  \n",
       "Iceland                                   0.591  \n",
       "Netherlands                               0.557  "
      ]
     },
     "execution_count": 102,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_hrep.set_index(\"Country or region\", inplace = True)\n",
    "df_hrep.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(188, 1)"
      ]
     },
     "execution_count": 103,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "corona_data.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(156, 4)"
      ]
     },
     "execution_count": 104,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_hrep.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Performing Inner Join"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>max_infect_rate</th>\n",
       "      <th>GDP per capita</th>\n",
       "      <th>Social support</th>\n",
       "      <th>Healthy life expectancy</th>\n",
       "      <th>Freedom to make life choices</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Afghanistan</th>\n",
       "      <td>915.0</td>\n",
       "      <td>0.350</td>\n",
       "      <td>0.517</td>\n",
       "      <td>0.361</td>\n",
       "      <td>0.000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Albania</th>\n",
       "      <td>82.0</td>\n",
       "      <td>0.947</td>\n",
       "      <td>0.848</td>\n",
       "      <td>0.874</td>\n",
       "      <td>0.383</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Algeria</th>\n",
       "      <td>199.0</td>\n",
       "      <td>1.002</td>\n",
       "      <td>1.160</td>\n",
       "      <td>0.785</td>\n",
       "      <td>0.086</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Argentina</th>\n",
       "      <td>2060.0</td>\n",
       "      <td>1.092</td>\n",
       "      <td>1.432</td>\n",
       "      <td>0.881</td>\n",
       "      <td>0.471</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Armenia</th>\n",
       "      <td>766.0</td>\n",
       "      <td>0.850</td>\n",
       "      <td>1.055</td>\n",
       "      <td>0.815</td>\n",
       "      <td>0.283</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             max_infect_rate  GDP per capita  Social support  \\\n",
       "Afghanistan            915.0           0.350           0.517   \n",
       "Albania                 82.0           0.947           0.848   \n",
       "Algeria                199.0           1.002           1.160   \n",
       "Argentina             2060.0           1.092           1.432   \n",
       "Armenia                766.0           0.850           1.055   \n",
       "\n",
       "             Healthy life expectancy  Freedom to make life choices  \n",
       "Afghanistan                    0.361                         0.000  \n",
       "Albania                        0.874                         0.383  \n",
       "Algeria                        0.785                         0.086  \n",
       "Argentina                      0.881                         0.471  \n",
       "Armenia                        0.815                         0.283  "
      ]
     },
     "execution_count": 105,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data = corona_data.join(df_hrep, how = \"inner\")\n",
    "data.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Correlation Matrix "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>max_infect_rate</th>\n",
       "      <th>GDP per capita</th>\n",
       "      <th>Social support</th>\n",
       "      <th>Healthy life expectancy</th>\n",
       "      <th>Freedom to make life choices</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>max_infect_rate</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.163941</td>\n",
       "      <td>0.129090</td>\n",
       "      <td>0.170824</td>\n",
       "      <td>0.043543</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>GDP per capita</th>\n",
       "      <td>0.163941</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.757521</td>\n",
       "      <td>0.859431</td>\n",
       "      <td>0.394799</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Social support</th>\n",
       "      <td>0.129090</td>\n",
       "      <td>0.757521</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.751632</td>\n",
       "      <td>0.456317</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Healthy life expectancy</th>\n",
       "      <td>0.170824</td>\n",
       "      <td>0.859431</td>\n",
       "      <td>0.751632</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.423146</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Freedom to make life choices</th>\n",
       "      <td>0.043543</td>\n",
       "      <td>0.394799</td>\n",
       "      <td>0.456317</td>\n",
       "      <td>0.423146</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                              max_infect_rate  GDP per capita  Social support  \\\n",
       "max_infect_rate                      1.000000        0.163941        0.129090   \n",
       "GDP per capita                       0.163941        1.000000        0.757521   \n",
       "Social support                       0.129090        0.757521        1.000000   \n",
       "Healthy life expectancy              0.170824        0.859431        0.751632   \n",
       "Freedom to make life choices         0.043543        0.394799        0.456317   \n",
       "\n",
       "                              Healthy life expectancy  \\\n",
       "max_infect_rate                              0.170824   \n",
       "GDP per capita                               0.859431   \n",
       "Social support                               0.751632   \n",
       "Healthy life expectancy                      1.000000   \n",
       "Freedom to make life choices                 0.423146   \n",
       "\n",
       "                              Freedom to make life choices  \n",
       "max_infect_rate                                   0.043543  \n",
       "GDP per capita                                    0.394799  \n",
       "Social support                                    0.456317  \n",
       "Healthy life expectancy                           0.423146  \n",
       "Freedom to make life choices                      1.000000  "
      ]
     },
     "execution_count": 106,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.corr()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Visualizing the results"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### GDP vs max_infect_rate"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x1edf26e6c08>"
      ]
     },
     "execution_count": 107,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "x = data[\"GDP per capita\"]\n",
    "y = data[\"max_infect_rate\"]\n",
    "sns.scatterplot(x, y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x1edf2733348>"
      ]
     },
     "execution_count": 108,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "x = data[\"GDP per capita\"]\n",
    "y = data[\"max_infect_rate\"]\n",
    "sns.scatterplot(x, np.log(y)) # apply logscalling to y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x1edf27c3e88>"
      ]
     },
     "execution_count": 109,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.regplot(x, np.log(y))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**_Peoples in developed countries are more prone to corona virus_**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
