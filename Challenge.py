{
 "cells": [
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "# Create a function that takes in three arguments:\n",
    "- Wikipedia data\n",
    "- Kaggle metadata\n",
    "- MovieLens rating data (from Kaggle)\n"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "- Create a function to turn the extracted values into a numeric value. \n",
    "- [found in LN 27] We’ll call it [def parse_dollars] and [def parse_dollars ] will take in a string and return a floating-point number. \n",
    "- We’ll start by making a skeleton function with comments explaining each step, and then fill in the steps with actual code."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# import dependencies \n",
    "import json\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import re\n",
    "\n",
    "file_dir = 'C:/Users/tenle/Documents/GitHub/Movies_ETL/Resources/'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Load th JSON into a List Dictionaries\n",
    "with open(f'{file_dir}/wikipedia.movies.json', mode='r') as file:wiki_movies_raw = json.load(file)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Add kaggle two dataframes into your project\n",
    "kaggle_metadata = pd.read_csv(f'{file_dir}movies_metadata.csv', low_memory=False)\n",
    "ratings = pd.read_csv(f'{file_dir}ratings.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "# list comprehension with the filter expression \n",
    "wiki_movies = [movie for movie in wiki_movies_raw\n",
    "               if ('Director' in movie or 'Directed by' in movie)\n",
    "                   and 'imdb_link' in movie\n",
    "                   and 'No. of episodes' not in movie] "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
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
       "      <th>url</th>\n",
       "      <th>year</th>\n",
       "      <th>imdb_link</th>\n",
       "      <th>title</th>\n",
       "      <th>Directed by</th>\n",
       "      <th>Produced by</th>\n",
       "      <th>Screenplay by</th>\n",
       "      <th>Story by</th>\n",
       "      <th>Based on</th>\n",
       "      <th>Starring</th>\n",
       "      <th>...</th>\n",
       "      <th>Predecessor</th>\n",
       "      <th>Founders</th>\n",
       "      <th>Area served</th>\n",
       "      <th>Products</th>\n",
       "      <th>Services</th>\n",
       "      <th>Russian</th>\n",
       "      <th>Hebrew</th>\n",
       "      <th>Revenue</th>\n",
       "      <th>Operating income</th>\n",
       "      <th>Polish</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>https://en.wikipedia.org/wiki/The_Adventures_o...</td>\n",
       "      <td>1990.0</td>\n",
       "      <td>https://www.imdb.com/title/tt0098987/</td>\n",
       "      <td>The Adventures of Ford Fairlane</td>\n",
       "      <td>Renny Harlin</td>\n",
       "      <td>[Steve Perry, Joel Silver]</td>\n",
       "      <td>[David Arnott, James Cappe, Daniel Waters]</td>\n",
       "      <td>[David Arnott, James Cappe]</td>\n",
       "      <td>[Characters, by Rex Weiner]</td>\n",
       "      <td>[Andrew Dice Clay, Wayne Newton, Priscilla Pre...</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>https://en.wikipedia.org/wiki/After_Dark,_My_S...</td>\n",
       "      <td>1990.0</td>\n",
       "      <td>https://www.imdb.com/title/tt0098994/</td>\n",
       "      <td>After Dark, My Sweet</td>\n",
       "      <td>James Foley</td>\n",
       "      <td>[Ric Kidney, Robert Redlin]</td>\n",
       "      <td>[James Foley, Robert Redlin]</td>\n",
       "      <td>NaN</td>\n",
       "      <td>[the novel, After Dark, My Sweet, by, Jim Thom...</td>\n",
       "      <td>[Jason Patric, Rachel Ward, Bruce Dern, George...</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>https://en.wikipedia.org/wiki/Air_America_(film)</td>\n",
       "      <td>1990.0</td>\n",
       "      <td>https://www.imdb.com/title/tt0099005/</td>\n",
       "      <td>Air America</td>\n",
       "      <td>Roger Spottiswoode</td>\n",
       "      <td>Daniel Melnick</td>\n",
       "      <td>[John Eskow, Richard Rush]</td>\n",
       "      <td>NaN</td>\n",
       "      <td>[Air America, by, Christopher Robbins]</td>\n",
       "      <td>[Mel Gibson, Robert Downey Jr., Nancy Travis, ...</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>https://en.wikipedia.org/wiki/Alice_(1990_film)</td>\n",
       "      <td>1990.0</td>\n",
       "      <td>https://www.imdb.com/title/tt0099012/</td>\n",
       "      <td>Alice</td>\n",
       "      <td>Woody Allen</td>\n",
       "      <td>Robert Greenhut</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>[Alec Baldwin, Blythe Danner, Judy Davis, Mia ...</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>https://en.wikipedia.org/wiki/Almost_an_Angel</td>\n",
       "      <td>1990.0</td>\n",
       "      <td>https://www.imdb.com/title/tt0099018/</td>\n",
       "      <td>Almost an Angel</td>\n",
       "      <td>John Cornell</td>\n",
       "      <td>John Cornell</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>[Paul Hogan, Elias Koteas, Linda Kozlowski]</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 193 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                                                 url    year  \\\n",
       "0  https://en.wikipedia.org/wiki/The_Adventures_o...  1990.0   \n",
       "1  https://en.wikipedia.org/wiki/After_Dark,_My_S...  1990.0   \n",
       "2   https://en.wikipedia.org/wiki/Air_America_(film)  1990.0   \n",
       "3    https://en.wikipedia.org/wiki/Alice_(1990_film)  1990.0   \n",
       "4      https://en.wikipedia.org/wiki/Almost_an_Angel  1990.0   \n",
       "\n",
       "                               imdb_link                            title  \\\n",
       "0  https://www.imdb.com/title/tt0098987/  The Adventures of Ford Fairlane   \n",
       "1  https://www.imdb.com/title/tt0098994/             After Dark, My Sweet   \n",
       "2  https://www.imdb.com/title/tt0099005/                      Air America   \n",
       "3  https://www.imdb.com/title/tt0099012/                            Alice   \n",
       "4  https://www.imdb.com/title/tt0099018/                  Almost an Angel   \n",
       "\n",
       "          Directed by                  Produced by  \\\n",
       "0        Renny Harlin   [Steve Perry, Joel Silver]   \n",
       "1         James Foley  [Ric Kidney, Robert Redlin]   \n",
       "2  Roger Spottiswoode               Daniel Melnick   \n",
       "3         Woody Allen              Robert Greenhut   \n",
       "4        John Cornell                 John Cornell   \n",
       "\n",
       "                                Screenplay by                     Story by  \\\n",
       "0  [David Arnott, James Cappe, Daniel Waters]  [David Arnott, James Cappe]   \n",
       "1                [James Foley, Robert Redlin]                          NaN   \n",
       "2                  [John Eskow, Richard Rush]                          NaN   \n",
       "3                                         NaN                          NaN   \n",
       "4                                         NaN                          NaN   \n",
       "\n",
       "                                            Based on  \\\n",
       "0                        [Characters, by Rex Weiner]   \n",
       "1  [the novel, After Dark, My Sweet, by, Jim Thom...   \n",
       "2             [Air America, by, Christopher Robbins]   \n",
       "3                                                NaN   \n",
       "4                                                NaN   \n",
       "\n",
       "                                            Starring  ... Predecessor  \\\n",
       "0  [Andrew Dice Clay, Wayne Newton, Priscilla Pre...  ...         NaN   \n",
       "1  [Jason Patric, Rachel Ward, Bruce Dern, George...  ...         NaN   \n",
       "2  [Mel Gibson, Robert Downey Jr., Nancy Travis, ...  ...         NaN   \n",
       "3  [Alec Baldwin, Blythe Danner, Judy Davis, Mia ...  ...         NaN   \n",
       "4        [Paul Hogan, Elias Koteas, Linda Kozlowski]  ...         NaN   \n",
       "\n",
       "  Founders Area served Products Services Russian Hebrew Revenue  \\\n",
       "0      NaN         NaN      NaN      NaN     NaN    NaN     NaN   \n",
       "1      NaN         NaN      NaN      NaN     NaN    NaN     NaN   \n",
       "2      NaN         NaN      NaN      NaN     NaN    NaN     NaN   \n",
       "3      NaN         NaN      NaN      NaN     NaN    NaN     NaN   \n",
       "4      NaN         NaN      NaN      NaN     NaN    NaN     NaN   \n",
       "\n",
       "  Operating income Polish  \n",
       "0              NaN    NaN  \n",
       "1              NaN    NaN  \n",
       "2              NaN    NaN  \n",
       "3              NaN    NaN  \n",
       "4              NaN    NaN  \n",
       "\n",
       "[5 rows x 193 columns]"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# wiki_movies DataFrame.\n",
    "wiki_movies_df = pd.DataFrame(wiki_movies_raw)\n",
    "wiki_movies_df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Create Function To Clean Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Function for cleaning movie data, use clean_movie\n",
    "\n",
    "def clean_movie(movie):\n",
    "    movie = dict(movie) #create a non-destructive copy\n",
    "    alt_titles = {}\n",
    "    # combine alternate titles into one list\n",
    "    for key in ['Also known as','Arabic','Cantonese','Chinese','French',\n",
    "                'Hangul','Hebrew','Hepburn','Japanese','Literally',\n",
    "                'Mandarin','McCune-Reischauer','Original title','Polish',\n",
    "                'Revised Romanization','Romanized','Russian',\n",
    "                'Simplified','Traditional','Yiddish']:\n",
    "        if key in movie:\n",
    "            alt_titles[key] = movie[key]\n",
    "            movie.pop(key)\n",
    "    if len(alt_titles) > 0:\n",
    "        movie['alt_titles'] = alt_titles\n",
    "\n",
    "    # merge column names\n",
    "    def change_column_name(old_name, new_name):\n",
    "        if old_name in movie:\n",
    "            movie[new_name] = movie.pop(old_name)\n",
    "    change_column_name('Adaptation by', 'Writer(s)')\n",
    "    change_column_name('Country of origin', 'Country')\n",
    "    change_column_name('Directed by', 'Director')\n",
    "    change_column_name('Distributed by', 'Distributor')\n",
    "    change_column_name('Edited by', 'Editor(s)')\n",
    "    change_column_name('Length', 'Running time')\n",
    "    change_column_name('Original release', 'Release date')\n",
    "    change_column_name('Music by', 'Composer(s)')\n",
    "    change_column_name('Produced by', 'Producer(s)')\n",
    "    change_column_name('Producer', 'Producer(s)')\n",
    "    change_column_name('Productioncompanies ', 'Production company(s)')\n",
    "    change_column_name('Productioncompany ', 'Production company(s)')\n",
    "    change_column_name('Released', 'Release Date')\n",
    "    change_column_name('Release Date', 'Release date')\n",
    "    change_column_name('Screen story by', 'Writer(s)')\n",
    "    change_column_name('Screenplay by', 'Writer(s)')\n",
    "    change_column_name('Story by', 'Writer(s)')\n",
    "    change_column_name('Theme music composer', 'Composer(s)')\n",
    "    change_column_name('Written by', 'Writer(s)')\n",
    "\n",
    "    return movie"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "clean_movies = [clean_movie(movie) for movie in wiki_movies]\n",
    "wiki_movies_df = pd.DataFrame(clean_movies)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Since we’re going to be using the IMDb ID to merge with the Kaggle data, we want to make sure that we don’t have any duplicate rows, according to the IMDb ID. First, we need to extract the IMDb ID from the IMDb link"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7076\n",
      "7033\n"
     ]
    },
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
       "      <th>url</th>\n",
       "      <th>year</th>\n",
       "      <th>imdb_link</th>\n",
       "      <th>title</th>\n",
       "      <th>Based on</th>\n",
       "      <th>Starring</th>\n",
       "      <th>Narrated by</th>\n",
       "      <th>Cinematography</th>\n",
       "      <th>Release date</th>\n",
       "      <th>Running time</th>\n",
       "      <th>...</th>\n",
       "      <th>Preceded by</th>\n",
       "      <th>Suggested by</th>\n",
       "      <th>alt_titles</th>\n",
       "      <th>Recorded</th>\n",
       "      <th>Venue</th>\n",
       "      <th>Label</th>\n",
       "      <th>Animation by</th>\n",
       "      <th>Color process</th>\n",
       "      <th>McCune–Reischauer</th>\n",
       "      <th>imdb_id</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>https://en.wikipedia.org/wiki/The_Adventures_o...</td>\n",
       "      <td>1990</td>\n",
       "      <td>https://www.imdb.com/title/tt0098987/</td>\n",
       "      <td>The Adventures of Ford Fairlane</td>\n",
       "      <td>[Characters, by Rex Weiner]</td>\n",
       "      <td>[Andrew Dice Clay, Wayne Newton, Priscilla Pre...</td>\n",
       "      <td>Andrew \"Dice\" Clay</td>\n",
       "      <td>Oliver Wood</td>\n",
       "      <td>[July 11, 1990, (, 1990-07-11, )]</td>\n",
       "      <td>102 minutes</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>tt0098987</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>https://en.wikipedia.org/wiki/After_Dark,_My_S...</td>\n",
       "      <td>1990</td>\n",
       "      <td>https://www.imdb.com/title/tt0098994/</td>\n",
       "      <td>After Dark, My Sweet</td>\n",
       "      <td>[the novel, After Dark, My Sweet, by, Jim Thom...</td>\n",
       "      <td>[Jason Patric, Rachel Ward, Bruce Dern, George...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Mark Plummer</td>\n",
       "      <td>[May 17, 1990, (, 1990-05-17, ), (Cannes Film ...</td>\n",
       "      <td>114 minutes</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>tt0098994</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>https://en.wikipedia.org/wiki/Air_America_(film)</td>\n",
       "      <td>1990</td>\n",
       "      <td>https://www.imdb.com/title/tt0099005/</td>\n",
       "      <td>Air America</td>\n",
       "      <td>[Air America, by, Christopher Robbins]</td>\n",
       "      <td>[Mel Gibson, Robert Downey Jr., Nancy Travis, ...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Roger Deakins</td>\n",
       "      <td>[August 10, 1990, (, 1990-08-10, )]</td>\n",
       "      <td>113 minutes</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>tt0099005</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>https://en.wikipedia.org/wiki/Alice_(1990_film)</td>\n",
       "      <td>1990</td>\n",
       "      <td>https://www.imdb.com/title/tt0099012/</td>\n",
       "      <td>Alice</td>\n",
       "      <td>NaN</td>\n",
       "      <td>[Alec Baldwin, Blythe Danner, Judy Davis, Mia ...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Carlo Di Palma</td>\n",
       "      <td>[December 25, 1990, (, 1990-12-25, )]</td>\n",
       "      <td>106 minutes</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>tt0099012</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>https://en.wikipedia.org/wiki/Almost_an_Angel</td>\n",
       "      <td>1990</td>\n",
       "      <td>https://www.imdb.com/title/tt0099018/</td>\n",
       "      <td>Almost an Angel</td>\n",
       "      <td>NaN</td>\n",
       "      <td>[Paul Hogan, Elias Koteas, Linda Kozlowski]</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Russell Boyd</td>\n",
       "      <td>December 19, 1990</td>\n",
       "      <td>95 minutes</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>tt0099018</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 41 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                                                 url  year  \\\n",
       "0  https://en.wikipedia.org/wiki/The_Adventures_o...  1990   \n",
       "1  https://en.wikipedia.org/wiki/After_Dark,_My_S...  1990   \n",
       "2   https://en.wikipedia.org/wiki/Air_America_(film)  1990   \n",
       "3    https://en.wikipedia.org/wiki/Alice_(1990_film)  1990   \n",
       "4      https://en.wikipedia.org/wiki/Almost_an_Angel  1990   \n",
       "\n",
       "                               imdb_link                            title  \\\n",
       "0  https://www.imdb.com/title/tt0098987/  The Adventures of Ford Fairlane   \n",
       "1  https://www.imdb.com/title/tt0098994/             After Dark, My Sweet   \n",
       "2  https://www.imdb.com/title/tt0099005/                      Air America   \n",
       "3  https://www.imdb.com/title/tt0099012/                            Alice   \n",
       "4  https://www.imdb.com/title/tt0099018/                  Almost an Angel   \n",
       "\n",
       "                                            Based on  \\\n",
       "0                        [Characters, by Rex Weiner]   \n",
       "1  [the novel, After Dark, My Sweet, by, Jim Thom...   \n",
       "2             [Air America, by, Christopher Robbins]   \n",
       "3                                                NaN   \n",
       "4                                                NaN   \n",
       "\n",
       "                                            Starring         Narrated by  \\\n",
       "0  [Andrew Dice Clay, Wayne Newton, Priscilla Pre...  Andrew \"Dice\" Clay   \n",
       "1  [Jason Patric, Rachel Ward, Bruce Dern, George...                 NaN   \n",
       "2  [Mel Gibson, Robert Downey Jr., Nancy Travis, ...                 NaN   \n",
       "3  [Alec Baldwin, Blythe Danner, Judy Davis, Mia ...                 NaN   \n",
       "4        [Paul Hogan, Elias Koteas, Linda Kozlowski]                 NaN   \n",
       "\n",
       "   Cinematography                                       Release date  \\\n",
       "0     Oliver Wood                  [July 11, 1990, (, 1990-07-11, )]   \n",
       "1    Mark Plummer  [May 17, 1990, (, 1990-05-17, ), (Cannes Film ...   \n",
       "2   Roger Deakins                [August 10, 1990, (, 1990-08-10, )]   \n",
       "3  Carlo Di Palma              [December 25, 1990, (, 1990-12-25, )]   \n",
       "4    Russell Boyd                                  December 19, 1990   \n",
       "\n",
       "  Running time  ... Preceded by Suggested by alt_titles Recorded Venue Label  \\\n",
       "0  102 minutes  ...         NaN          NaN        NaN      NaN   NaN   NaN   \n",
       "1  114 minutes  ...         NaN          NaN        NaN      NaN   NaN   NaN   \n",
       "2  113 minutes  ...         NaN          NaN        NaN      NaN   NaN   NaN   \n",
       "3  106 minutes  ...         NaN          NaN        NaN      NaN   NaN   NaN   \n",
       "4   95 minutes  ...         NaN          NaN        NaN      NaN   NaN   NaN   \n",
       "\n",
       "  Animation by Color process McCune–Reischauer    imdb_id  \n",
       "0          NaN           NaN               NaN  tt0098987  \n",
       "1          NaN           NaN               NaN  tt0098994  \n",
       "2          NaN           NaN               NaN  tt0099005  \n",
       "3          NaN           NaN               NaN  tt0099012  \n",
       "4          NaN           NaN               NaN  tt0099018  \n",
       "\n",
       "[5 rows x 41 columns]"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "wiki_movies_df['imdb_id'] = wiki_movies_df['imdb_link'].str.extract(r'(tt\\d{7})')\n",
    "print(len(wiki_movies_df))\n",
    "\n",
    "# we only want to consider the IMDb ID, use the subset argument, and set inplace equal to \"True\n",
    "wiki_movies_df.drop_duplicates(subset='imdb_id', inplace=True) # no copy of the object\n",
    "print(len(wiki_movies_df))\n",
    "wiki_movies_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Remove null columns\n",
    "wiki_columns_to_keep = [column for column in wiki_movies_df.columns if wiki_movies_df[column].isnull().sum() < len(wiki_movies_df) * 0.9]\n",
    "wiki_movies_df = wiki_movies_df[wiki_columns_to_keep]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
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
       "      <th>url</th>\n",
       "      <th>year</th>\n",
       "      <th>imdb_link</th>\n",
       "      <th>title</th>\n",
       "      <th>Based on</th>\n",
       "      <th>Starring</th>\n",
       "      <th>Cinematography</th>\n",
       "      <th>Release date</th>\n",
       "      <th>Running time</th>\n",
       "      <th>Country</th>\n",
       "      <th>...</th>\n",
       "      <th>Budget</th>\n",
       "      <th>Box office</th>\n",
       "      <th>Director</th>\n",
       "      <th>Distributor</th>\n",
       "      <th>Editor(s)</th>\n",
       "      <th>Composer(s)</th>\n",
       "      <th>Producer(s)</th>\n",
       "      <th>Production company(s)</th>\n",
       "      <th>Writer(s)</th>\n",
       "      <th>imdb_id</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>https://en.wikipedia.org/wiki/The_Adventures_o...</td>\n",
       "      <td>1990</td>\n",
       "      <td>https://www.imdb.com/title/tt0098987/</td>\n",
       "      <td>The Adventures of Ford Fairlane</td>\n",
       "      <td>[Characters, by Rex Weiner]</td>\n",
       "      <td>[Andrew Dice Clay, Wayne Newton, Priscilla Pre...</td>\n",
       "      <td>Oliver Wood</td>\n",
       "      <td>[July 11, 1990, (, 1990-07-11, )]</td>\n",
       "      <td>102 minutes</td>\n",
       "      <td>United States</td>\n",
       "      <td>...</td>\n",
       "      <td>$20 million</td>\n",
       "      <td>$21.4 million</td>\n",
       "      <td>Renny Harlin</td>\n",
       "      <td>20th Century Fox</td>\n",
       "      <td>Michael Tronick</td>\n",
       "      <td>[Cliff Eidelman, Yello]</td>\n",
       "      <td>[Steve Perry, Joel Silver]</td>\n",
       "      <td>Silver Pictures</td>\n",
       "      <td>[David Arnott, James Cappe]</td>\n",
       "      <td>tt0098987</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>https://en.wikipedia.org/wiki/After_Dark,_My_S...</td>\n",
       "      <td>1990</td>\n",
       "      <td>https://www.imdb.com/title/tt0098994/</td>\n",
       "      <td>After Dark, My Sweet</td>\n",
       "      <td>[the novel, After Dark, My Sweet, by, Jim Thom...</td>\n",
       "      <td>[Jason Patric, Rachel Ward, Bruce Dern, George...</td>\n",
       "      <td>Mark Plummer</td>\n",
       "      <td>[May 17, 1990, (, 1990-05-17, ), (Cannes Film ...</td>\n",
       "      <td>114 minutes</td>\n",
       "      <td>United States</td>\n",
       "      <td>...</td>\n",
       "      <td>$6 million</td>\n",
       "      <td>$2.7 million</td>\n",
       "      <td>James Foley</td>\n",
       "      <td>Avenue Pictures</td>\n",
       "      <td>Howard E. Smith</td>\n",
       "      <td>Maurice Jarre</td>\n",
       "      <td>[Ric Kidney, Robert Redlin]</td>\n",
       "      <td>Avenue Pictures</td>\n",
       "      <td>[James Foley, Robert Redlin]</td>\n",
       "      <td>tt0098994</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>https://en.wikipedia.org/wiki/Air_America_(film)</td>\n",
       "      <td>1990</td>\n",
       "      <td>https://www.imdb.com/title/tt0099005/</td>\n",
       "      <td>Air America</td>\n",
       "      <td>[Air America, by, Christopher Robbins]</td>\n",
       "      <td>[Mel Gibson, Robert Downey Jr., Nancy Travis, ...</td>\n",
       "      <td>Roger Deakins</td>\n",
       "      <td>[August 10, 1990, (, 1990-08-10, )]</td>\n",
       "      <td>113 minutes</td>\n",
       "      <td>United States</td>\n",
       "      <td>...</td>\n",
       "      <td>$35 million</td>\n",
       "      <td>$57,718,089</td>\n",
       "      <td>Roger Spottiswoode</td>\n",
       "      <td>TriStar Pictures</td>\n",
       "      <td>[John Bloom, Lois Freeman-Fox]</td>\n",
       "      <td>Charles Gross</td>\n",
       "      <td>Daniel Melnick</td>\n",
       "      <td>[Carolco Pictures, IndieProd Company]</td>\n",
       "      <td>[John Eskow, Richard Rush]</td>\n",
       "      <td>tt0099005</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>https://en.wikipedia.org/wiki/Alice_(1990_film)</td>\n",
       "      <td>1990</td>\n",
       "      <td>https://www.imdb.com/title/tt0099012/</td>\n",
       "      <td>Alice</td>\n",
       "      <td>NaN</td>\n",
       "      <td>[Alec Baldwin, Blythe Danner, Judy Davis, Mia ...</td>\n",
       "      <td>Carlo Di Palma</td>\n",
       "      <td>[December 25, 1990, (, 1990-12-25, )]</td>\n",
       "      <td>106 minutes</td>\n",
       "      <td>United States</td>\n",
       "      <td>...</td>\n",
       "      <td>$12 million</td>\n",
       "      <td>$7,331,647</td>\n",
       "      <td>Woody Allen</td>\n",
       "      <td>Orion Pictures</td>\n",
       "      <td>Susan E. Morse</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Robert Greenhut</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Woody Allen</td>\n",
       "      <td>tt0099012</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>https://en.wikipedia.org/wiki/Almost_an_Angel</td>\n",
       "      <td>1990</td>\n",
       "      <td>https://www.imdb.com/title/tt0099018/</td>\n",
       "      <td>Almost an Angel</td>\n",
       "      <td>NaN</td>\n",
       "      <td>[Paul Hogan, Elias Koteas, Linda Kozlowski]</td>\n",
       "      <td>Russell Boyd</td>\n",
       "      <td>December 19, 1990</td>\n",
       "      <td>95 minutes</td>\n",
       "      <td>US</td>\n",
       "      <td>...</td>\n",
       "      <td>$25 million</td>\n",
       "      <td>$6,939,946 (USA)</td>\n",
       "      <td>John Cornell</td>\n",
       "      <td>Paramount Pictures</td>\n",
       "      <td>David Stiven</td>\n",
       "      <td>Maurice Jarre</td>\n",
       "      <td>John Cornell</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Paul Hogan</td>\n",
       "      <td>tt0099018</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 21 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                                                 url  year  \\\n",
       "0  https://en.wikipedia.org/wiki/The_Adventures_o...  1990   \n",
       "1  https://en.wikipedia.org/wiki/After_Dark,_My_S...  1990   \n",
       "2   https://en.wikipedia.org/wiki/Air_America_(film)  1990   \n",
       "3    https://en.wikipedia.org/wiki/Alice_(1990_film)  1990   \n",
       "4      https://en.wikipedia.org/wiki/Almost_an_Angel  1990   \n",
       "\n",
       "                               imdb_link                            title  \\\n",
       "0  https://www.imdb.com/title/tt0098987/  The Adventures of Ford Fairlane   \n",
       "1  https://www.imdb.com/title/tt0098994/             After Dark, My Sweet   \n",
       "2  https://www.imdb.com/title/tt0099005/                      Air America   \n",
       "3  https://www.imdb.com/title/tt0099012/                            Alice   \n",
       "4  https://www.imdb.com/title/tt0099018/                  Almost an Angel   \n",
       "\n",
       "                                            Based on  \\\n",
       "0                        [Characters, by Rex Weiner]   \n",
       "1  [the novel, After Dark, My Sweet, by, Jim Thom...   \n",
       "2             [Air America, by, Christopher Robbins]   \n",
       "3                                                NaN   \n",
       "4                                                NaN   \n",
       "\n",
       "                                            Starring  Cinematography  \\\n",
       "0  [Andrew Dice Clay, Wayne Newton, Priscilla Pre...     Oliver Wood   \n",
       "1  [Jason Patric, Rachel Ward, Bruce Dern, George...    Mark Plummer   \n",
       "2  [Mel Gibson, Robert Downey Jr., Nancy Travis, ...   Roger Deakins   \n",
       "3  [Alec Baldwin, Blythe Danner, Judy Davis, Mia ...  Carlo Di Palma   \n",
       "4        [Paul Hogan, Elias Koteas, Linda Kozlowski]    Russell Boyd   \n",
       "\n",
       "                                        Release date Running time  \\\n",
       "0                  [July 11, 1990, (, 1990-07-11, )]  102 minutes   \n",
       "1  [May 17, 1990, (, 1990-05-17, ), (Cannes Film ...  114 minutes   \n",
       "2                [August 10, 1990, (, 1990-08-10, )]  113 minutes   \n",
       "3              [December 25, 1990, (, 1990-12-25, )]  106 minutes   \n",
       "4                                  December 19, 1990   95 minutes   \n",
       "\n",
       "         Country  ...       Budget        Box office            Director  \\\n",
       "0  United States  ...  $20 million     $21.4 million        Renny Harlin   \n",
       "1  United States  ...   $6 million      $2.7 million         James Foley   \n",
       "2  United States  ...  $35 million       $57,718,089  Roger Spottiswoode   \n",
       "3  United States  ...  $12 million        $7,331,647         Woody Allen   \n",
       "4             US  ...  $25 million  $6,939,946 (USA)        John Cornell   \n",
       "\n",
       "          Distributor                       Editor(s)  \\\n",
       "0    20th Century Fox                 Michael Tronick   \n",
       "1     Avenue Pictures                 Howard E. Smith   \n",
       "2    TriStar Pictures  [John Bloom, Lois Freeman-Fox]   \n",
       "3      Orion Pictures                  Susan E. Morse   \n",
       "4  Paramount Pictures                    David Stiven   \n",
       "\n",
       "               Composer(s)                  Producer(s)  \\\n",
       "0  [Cliff Eidelman, Yello]   [Steve Perry, Joel Silver]   \n",
       "1            Maurice Jarre  [Ric Kidney, Robert Redlin]   \n",
       "2            Charles Gross               Daniel Melnick   \n",
       "3                      NaN              Robert Greenhut   \n",
       "4            Maurice Jarre                 John Cornell   \n",
       "\n",
       "                   Production company(s)                     Writer(s)  \\\n",
       "0                        Silver Pictures   [David Arnott, James Cappe]   \n",
       "1                        Avenue Pictures  [James Foley, Robert Redlin]   \n",
       "2  [Carolco Pictures, IndieProd Company]    [John Eskow, Richard Rush]   \n",
       "3                                    NaN                   Woody Allen   \n",
       "4                                    NaN                    Paul Hogan   \n",
       "\n",
       "     imdb_id  \n",
       "0  tt0098987  \n",
       "1  tt0098994  \n",
       "2  tt0099005  \n",
       "3  tt0099012  \n",
       "4  tt0099018  \n",
       "\n",
       "[5 rows x 21 columns]"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "wiki_movies_df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Make a Plan to Convert and Parse the Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "# first we’ll make a data series that drops missing values, start with box office\n",
    "box_office = wiki_movies_df['Box office'].dropna() "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "# second we’ll need to make sure all of the box office data is entered as a string.\n",
    "# create a function is_not_a_string to return a value !=str\n",
    "def is_not_a_string(x):\n",
    "    return type(x) != str\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "34                           [US$, 4,212,828]\n",
       "54      [$6,698,361 (, United States, ), [2]]\n",
       "74                    [$6,488,144, (US), [1]]\n",
       "126                [US$1,531,489, (domestic)]\n",
       "130                          [US$, 4,803,039]\n",
       "                        ...                  \n",
       "6980               [$99.6, million, [4], [5]]\n",
       "6994                   [$365.6, million, [1]]\n",
       "6995                         [$53.8, million]\n",
       "7015                     [$435, million, [7]]\n",
       "7048                   [$529.3, million, [4]]\n",
       "Name: Box office, Length: 135, dtype: object"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# add the string function\n",
    "box_office[box_office.map(is_not_a_string)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "34                           [US$, 4,212,828]\n",
       "54      [$6,698,361 (, United States, ), [2]]\n",
       "74                    [$6,488,144, (US), [1]]\n",
       "126                [US$1,531,489, (domestic)]\n",
       "130                          [US$, 4,803,039]\n",
       "                        ...                  \n",
       "6980               [$99.6, million, [4], [5]]\n",
       "6994                   [$365.6, million, [1]]\n",
       "6995                         [$53.8, million]\n",
       "7015                     [$435, million, [7]]\n",
       "7048                   [$529.3, million, [4]]\n",
       "Name: Box office, Length: 135, dtype: object"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use lambdafunction to ensure all of the box office data is entered as a string\n",
    "box_office[box_office.map(lambda x: type(x) != str)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0       $21.4 million\n",
       "1        $2.7 million\n",
       "2         $57,718,089\n",
       "3          $7,331,647\n",
       "4    $6,939,946 (USA)\n",
       "Name: Box office, dtype: object"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use join() string method to remove the data points that are stored as lists\n",
    "box_office = box_office.apply(lambda x: ' '.join(x) if type(x) == list else x)\n",
    "box_office.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Remember, there are two main forms the box office data is written in: “$123.4 million” (or billion), and “$123,456,789.” \n",
    "We’re going to build a regular expression for each form, and then see what forms are left over."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Preface the string with an r for the escape characters to remain.\n",
    "form_one = r'\\$\\d+\\.?\\d*\\s*[mb]illion'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Preface the string with an r for the escape characters to remain.\n",
    "form_two = r'\\$\\d{1,3}(?:,\\d{3})+'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4930      $36.1 million [1] $8,610,119 (US DVD sales) [3]\n",
       "6358    $18,687,388 (Theatrical Performance) [4] $1,26...\n",
       "Name: Box office, dtype: object"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Create two Boolean Series called matches_form_one and matches_form_two\n",
    "import re\n",
    "matches_form_one = box_office.str.contains(form_one, flags=re.IGNORECASE)\n",
    "matches_form_two = box_office.str.contains(form_two, flags=re.IGNORECASE)\n",
    "box_office[matches_form_one & matches_form_two]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "form_one = r'\\$\\s*\\d+\\.?\\d*\\s*[mb]illi?on'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Change form_two to allow for either a comma or period as a thousands separator\n",
    "form_two = r'\\$\\s*\\d{1,3}(?:[,\\.]\\d{3})+(?!\\s[mb]illion)'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "box_office = box_office.str.replace(r'\\$.*[-—–](?![a-z])', '$', regex=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Use the expressions to extract only the parts of the strings that match"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "def parse_dollars(s):\n",
    "    # if s is not a string, return NaN\n",
    "    if type(s) != str:\n",
    "        return np.nan\n",
    "\n",
    "    # if input is of the form $###.# million\n",
    "    if re.match(r'\\$\\s*\\d+\\.?\\d*\\s*milli?on', s, flags=re.IGNORECASE):\n",
    "\n",
    "        # remove dollar sign and \" million\"\n",
    "        s = re.sub('\\$|\\s|[a-zA-Z]','', s)\n",
    "\n",
    "        # convert to float and multiply by a million\n",
    "        value = float(s) * 10**6\n",
    "\n",
    "        # return value\n",
    "        return value\n",
    "\n",
    "    # if input is of the form $###.# billion\n",
    "    elif re.match(r'\\$\\s*\\d+\\.?\\d*\\s*billi?on', s, flags=re.IGNORECASE):\n",
    "\n",
    "        # remove dollar sign and \" billion\"\n",
    "        s = re.sub('\\$|\\s|[a-zA-Z]','', s)\n",
    "\n",
    "        # convert to float and multiply by a billion\n",
    "        value = float(s) * 10**9\n",
    "\n",
    "        # return value\n",
    "        return value\n",
    "\n",
    "    # if input is of the form $###,###,###\n",
    "    elif re.match(r'\\$\\s*\\d{1,3}(?:[,\\.]\\d{3})+(?!\\s[mb]illion)', s, flags=re.IGNORECASE):\n",
    "\n",
    "        # remove dollar sign and commas\n",
    "        s = re.sub('\\$|,','', s)\n",
    "\n",
    "        # convert to float\n",
    "        value = float(s)\n",
    "\n",
    "        # return value\n",
    "        return value\n",
    "\n",
    "    # otherwise, return NaN\n",
    "    else:\n",
    "        return np.nan"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "First, we need to extract the values from box_office using str.extract. Then we'll apply parse_dollars to the first column in the DataFrame returned by str.extract, which in code looks like the following:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "wiki_movies_df['box_office'] = box_office.str.extract(f'({form_one}|{form_two})', flags=re.IGNORECASE)[0].apply(parse_dollars)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "wiki_movies_df.drop('Box office', axis=1, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "budget = wiki_movies_df['Budget'].dropna()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Convert any lists to strings:\n",
    "budget = budget.map(lambda x: ' '.join(x) if type(x) == list else x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "budget = budget.str.replace(r'\\$.*[-—–](?![a-z])', '$', regex=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "136                         Unknown\n",
       "204     60 million Norwegian Kroner\n",
       "478                         Unknown\n",
       "973             $34 [3] [4] million\n",
       "1126               $120 [4] million\n",
       "1226                        Unknown\n",
       "1278                            HBO\n",
       "1374                     £6,000,000\n",
       "1397                     13 million\n",
       "1480                   £2.8 million\n",
       "1734                   CAD2,000,000\n",
       "1913     PHP 85 million (estimated)\n",
       "1948                    102,888,900\n",
       "1953                   3,500,000 DM\n",
       "1973                     ₤2,300,874\n",
       "2281                     $14 milion\n",
       "2451                     ₤6,350,000\n",
       "3144                   € 40 million\n",
       "3360               $150 [6] million\n",
       "3418                        $218.32\n",
       "3802                   £4.2 million\n",
       "3906                            N/A\n",
       "3959                    760,000 USD\n",
       "4470                       19 crore\n",
       "4641                    £17 million\n",
       "5034              $$200 [4] million\n",
       "5055           $155 [2] [3] million\n",
       "5419                $40 [4] million\n",
       "5424                            N/A\n",
       "5447                     £4 million\n",
       "5671                    €14 million\n",
       "5687                   $ dead link]\n",
       "6385               £ 12 million [3]\n",
       "6593                     £3 million\n",
       "6821                  £12.9 million\n",
       "6843                      3.5 crore\n",
       "6895                        919,000\n",
       "7070                   €4.3 million\n",
       "Name: Budget, dtype: object"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Create two Boolean Series called matches_form_one and matches_form_two, \n",
    "matches_form_one = budget.str.contains(form_one, flags=re.IGNORECASE)\n",
    "matches_form_two = budget.str.contains(form_two, flags=re.IGNORECASE)\n",
    "budget[~matches_form_one & ~matches_form_two]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "136                         Unknown\n",
       "204     60 million Norwegian Kroner\n",
       "478                         Unknown\n",
       "973                     $34 million\n",
       "1126                   $120 million\n",
       "1226                        Unknown\n",
       "1278                            HBO\n",
       "1374                     £6,000,000\n",
       "1397                     13 million\n",
       "1480                   £2.8 million\n",
       "1734                   CAD2,000,000\n",
       "1913     PHP 85 million (estimated)\n",
       "1948                    102,888,900\n",
       "1953                   3,500,000 DM\n",
       "1973                     ₤2,300,874\n",
       "2281                     $14 milion\n",
       "2451                     ₤6,350,000\n",
       "3144                   € 40 million\n",
       "3360                   $150 million\n",
       "3418                        $218.32\n",
       "3802                   £4.2 million\n",
       "3906                            N/A\n",
       "3959                    760,000 USD\n",
       "4470                       19 crore\n",
       "4641                    £17 million\n",
       "5034                  $$200 million\n",
       "5055                   $155 million\n",
       "5419                    $40 million\n",
       "5424                            N/A\n",
       "5447                     £4 million\n",
       "5671                    €14 million\n",
       "5687                   $ dead link]\n",
       "6385                  £ 12 million \n",
       "6593                     £3 million\n",
       "6821                  £12.9 million\n",
       "6843                      3.5 crore\n",
       "6895                        919,000\n",
       "7070                   €4.3 million\n",
       "Name: Budget, dtype: object"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# remove  citations  references\n",
    "budget = budget.str.replace(r'\\[\\d+\\]\\s*', '')\n",
    "budget[~matches_form_one & ~matches_form_two]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Parse the budget values\n",
    "wiki_movies_df['budget'] = budget.str.extract(f'({form_one}|{form_two})', flags=re.IGNORECASE)[0].apply(parse_dollars)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Drop  Budget column.\n",
    "wiki_movies_df.drop('Budget', axis=1, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Release date variable using lambda\n",
    "release_date = wiki_movies_df['Release date'].dropna().apply(lambda x: ' '.join(x) if type(x) == list else x)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The forms we’ll be parsing are:\n",
    "\n",
    "    Full month name, one- to two-digit day, four-digit year (i.e., January 1, 2000)\n",
    "    Four-digit year, two-digit month, two-digit day, with any separator (i.e., 2000-01-01)\n",
    "    Full month name, four-digit year (i.e., January 2000)\n",
    "    Four-digit year\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [],
   "source": [
    "date_form_one = r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\\s[123]\\d,\\s\\d{4}'\n",
    "date_form_two = r'\\d{4}.[01]\\d.[123]\\d'\n",
    "date_form_three = r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\\s\\d{4}'\n",
    "date_form_four = r'\\d{4}'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [],
   "source": [
    "wiki_movies_df['release_date'] = pd.to_datetime(release_date.str.extract(f'({date_form_one}|{date_form_two}|{date_form_three}|{date_form_four})')[0], infer_datetime_format=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Parse Running Time\n",
    "First, make a variable that holds the non-null values of Release date in the DataFrame, converting lists to strings"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "running_time = wiki_movies_df['Running time'].dropna().apply(lambda x: ' '.join(x) if type(x) == list else x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [],
   "source": [
    "running_time_extract = running_time.str.extract(r'(\\d+)\\s*ho?u?r?s?\\s*(\\d*)|(\\d+)\\s*m')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "running_time_extract = running_time_extract.apply(lambda col: pd.to_numeric(col, errors='coerce')).fillna(0)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now we can apply a function that will convert the hour capture groups and minute capture groups to minutes if the pure minutes capture group is zero, and save the output to wiki_movies_df:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [],
   "source": [
    "wiki_movies_df['running_time'] = running_time_extract.apply(lambda row: row[0]*60 + row[1] if row[2] == 0 else row[2], axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Drop Running time from the dataset with the following code:\n",
    "wiki_movies_df.drop('Running time', axis=1, inplace=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Clean Kaggle Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "adult                     object\n",
       "belongs_to_collection     object\n",
       "budget                    object\n",
       "genres                    object\n",
       "homepage                  object\n",
       "id                        object\n",
       "imdb_id                   object\n",
       "original_language         object\n",
       "original_title            object\n",
       "overview                  object\n",
       "popularity                object\n",
       "poster_path               object\n",
       "production_companies      object\n",
       "production_countries      object\n",
       "release_date              object\n",
       "revenue                  float64\n",
       "runtime                  float64\n",
       "spoken_languages          object\n",
       "status                    object\n",
       "tagline                   object\n",
       "title                     object\n",
       "video                     object\n",
       "vote_average             float64\n",
       "vote_count               float64\n",
       "dtype: object"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "kaggle_metadata.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False                                                                                                                             45454\n",
       "True                                                                                                                                  9\n",
       " - Written by Ørnås                                                                                                                   1\n",
       " Rune Balot goes to a casino connected to the October corporation to try to wrap up her case once and for all.                        1\n",
       " Avalanche Sharks tells the story of a bikini contest that turns into a horrifying affair when it is hit by a shark avalanche.        1\n",
       "Name: adult, dtype: int64"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Check values are either True or False.\n",
    "kaggle_metadata['adult'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
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
       "      <th>adult</th>\n",
       "      <th>belongs_to_collection</th>\n",
       "      <th>budget</th>\n",
       "      <th>genres</th>\n",
       "      <th>homepage</th>\n",
       "      <th>id</th>\n",
       "      <th>imdb_id</th>\n",
       "      <th>original_language</th>\n",
       "      <th>original_title</th>\n",
       "      <th>overview</th>\n",
       "      <th>...</th>\n",
       "      <th>release_date</th>\n",
       "      <th>revenue</th>\n",
       "      <th>runtime</th>\n",
       "      <th>spoken_languages</th>\n",
       "      <th>status</th>\n",
       "      <th>tagline</th>\n",
       "      <th>title</th>\n",
       "      <th>video</th>\n",
       "      <th>vote_average</th>\n",
       "      <th>vote_count</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>19730</th>\n",
       "      <td>- Written by Ørnås</td>\n",
       "      <td>0.065736</td>\n",
       "      <td>/ff9qCepilowshEtG2GYWwzt2bs4.jpg</td>\n",
       "      <td>[{'name': 'Carousel Productions', 'id': 11176}...</td>\n",
       "      <td>[{'iso_3166_1': 'CA', 'name': 'Canada'}, {'iso...</td>\n",
       "      <td>1997-08-20</td>\n",
       "      <td>0</td>\n",
       "      <td>104.0</td>\n",
       "      <td>[{'iso_639_1': 'en', 'name': 'English'}]</td>\n",
       "      <td>Released</td>\n",
       "      <td>...</td>\n",
       "      <td>1</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>29503</th>\n",
       "      <td>Rune Balot goes to a casino connected to the ...</td>\n",
       "      <td>1.931659</td>\n",
       "      <td>/zV8bHuSL6WXoD6FWogP9j4x80bL.jpg</td>\n",
       "      <td>[{'name': 'Aniplex', 'id': 2883}, {'name': 'Go...</td>\n",
       "      <td>[{'iso_3166_1': 'US', 'name': 'United States o...</td>\n",
       "      <td>2012-09-29</td>\n",
       "      <td>0</td>\n",
       "      <td>68.0</td>\n",
       "      <td>[{'iso_639_1': 'ja', 'name': '日本語'}]</td>\n",
       "      <td>Released</td>\n",
       "      <td>...</td>\n",
       "      <td>12</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>35587</th>\n",
       "      <td>Avalanche Sharks tells the story of a bikini ...</td>\n",
       "      <td>2.185485</td>\n",
       "      <td>/zaSf5OG7V8X8gqFvly88zDdRm46.jpg</td>\n",
       "      <td>[{'name': 'Odyssey Media', 'id': 17161}, {'nam...</td>\n",
       "      <td>[{'iso_3166_1': 'CA', 'name': 'Canada'}]</td>\n",
       "      <td>2014-01-01</td>\n",
       "      <td>0</td>\n",
       "      <td>82.0</td>\n",
       "      <td>[{'iso_639_1': 'en', 'name': 'English'}]</td>\n",
       "      <td>Released</td>\n",
       "      <td>...</td>\n",
       "      <td>22</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>3 rows × 24 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                                                   adult  \\\n",
       "19730                                 - Written by Ørnås   \n",
       "29503   Rune Balot goes to a casino connected to the ...   \n",
       "35587   Avalanche Sharks tells the story of a bikini ...   \n",
       "\n",
       "      belongs_to_collection                            budget  \\\n",
       "19730              0.065736  /ff9qCepilowshEtG2GYWwzt2bs4.jpg   \n",
       "29503              1.931659  /zV8bHuSL6WXoD6FWogP9j4x80bL.jpg   \n",
       "35587              2.185485  /zaSf5OG7V8X8gqFvly88zDdRm46.jpg   \n",
       "\n",
       "                                                  genres  \\\n",
       "19730  [{'name': 'Carousel Productions', 'id': 11176}...   \n",
       "29503  [{'name': 'Aniplex', 'id': 2883}, {'name': 'Go...   \n",
       "35587  [{'name': 'Odyssey Media', 'id': 17161}, {'nam...   \n",
       "\n",
       "                                                homepage          id imdb_id  \\\n",
       "19730  [{'iso_3166_1': 'CA', 'name': 'Canada'}, {'iso...  1997-08-20       0   \n",
       "29503  [{'iso_3166_1': 'US', 'name': 'United States o...  2012-09-29       0   \n",
       "35587           [{'iso_3166_1': 'CA', 'name': 'Canada'}]  2014-01-01       0   \n",
       "\n",
       "      original_language                            original_title  overview  \\\n",
       "19730             104.0  [{'iso_639_1': 'en', 'name': 'English'}]  Released   \n",
       "29503              68.0      [{'iso_639_1': 'ja', 'name': '日本語'}]  Released   \n",
       "35587              82.0  [{'iso_639_1': 'en', 'name': 'English'}]  Released   \n",
       "\n",
       "       ... release_date revenue runtime spoken_languages status  tagline  \\\n",
       "19730  ...            1     NaN     NaN              NaN    NaN      NaN   \n",
       "29503  ...           12     NaN     NaN              NaN    NaN      NaN   \n",
       "35587  ...           22     NaN     NaN              NaN    NaN      NaN   \n",
       "\n",
       "       title video vote_average vote_count  \n",
       "19730    NaN   NaN          NaN        NaN  \n",
       "29503    NaN   NaN          NaN        NaN  \n",
       "35587    NaN   NaN          NaN        NaN  \n",
       "\n",
       "[3 rows x 24 columns]"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "kaggle_metadata[~kaggle_metadata['adult'].isin(['True','False'])]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [],
   "source": [
    "kaggle_metadata = kaggle_metadata[kaggle_metadata['adult'] == 'False'].drop('adult',axis='columns')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False    45358\n",
       "True        93\n",
       "Name: video, dtype: int64"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "kaggle_metadata['video'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [],
   "source": [
    "kaggle_metadata['video'] = kaggle_metadata['video'] == 'True'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [],
   "source": [
    "kaggle_metadata['budget'] = kaggle_metadata['budget'].astype(int)\n",
    "kaggle_metadata['id'] = pd.to_numeric(kaggle_metadata['id'], errors='raise')\n",
    "kaggle_metadata['popularity'] = pd.to_numeric(kaggle_metadata['popularity'], errors='raise')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Convert release_date to to_datetime().\n",
    "kaggle_metadata['release_date'] = pd.to_datetime(kaggle_metadata['release_date'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Assign it to the timestamp column.\n",
    "ratings['timestamp'] = pd.to_datetime(ratings['timestamp'], unit='s')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Merge  IMDb ID.\n",
    "movies_df = pd.merge(wiki_movies_df, kaggle_metadata, on='imdb_id', suffixes=['_wiki','_kaggle'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['url', 'year', 'imdb_link', 'title_wiki', 'Based on', 'Starring',\n",
       "       'Cinematography', 'Release date', 'Country', 'Language', 'Director',\n",
       "       'Distributor', 'Editor(s)', 'Composer(s)', 'Producer(s)',\n",
       "       'Production company(s)', 'Writer(s)', 'imdb_id', 'box_office',\n",
       "       'budget_wiki', 'release_date_wiki', 'running_time',\n",
       "       'belongs_to_collection', 'budget_kaggle', 'genres', 'homepage', 'id',\n",
       "       'original_language', 'original_title', 'overview', 'popularity',\n",
       "       'poster_path', 'production_companies', 'production_countries',\n",
       "       'release_date_kaggle', 'revenue', 'runtime', 'spoken_languages',\n",
       "       'status', 'tagline', 'title_kaggle', 'video', 'vote_average',\n",
       "       'vote_count'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movies_df.columns"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Assumption: \n",
    "As shown in the data above, it is inidcated the there are 7 instances of similar data from Wiki and MovieLens\n",
    "\n",
    "- Similar Data from  Wiki and MovieLens\n",
    "- box_office : revenue\n",
    "- release_date_wiki : release_data_kaggle\n",
    "- title_wiki : title_kaggle\n",
    "- budget_wiki : budget_kaggle\n",
    "- Production company(s) : production_companies\n",
    "- running_time : runtime\n",
    "- Language : originale_language\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Drop the title_wiki, release_date_wiki, Language, and Production company(s) columns.\n",
    "movies_df.drop(columns=['title_wiki','release_date_wiki','Language','Production company(s)'], inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a function that fills missing data and drop redundant column.\n",
    "def fill_missing_kaggle_data(df, kaggle_column, wiki_column):\n",
    "    df[kaggle_column] = df.apply(\n",
    "        lambda row: row[wiki_column] if row[kaggle_column] == 0 else row[kaggle_column]\n",
    "        , axis=1)\n",
    "    df.drop(columns=wiki_column, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x1f203e85808>"
      ]
     },
     "execution_count": 95,
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
    "movies_df.fillna(0).plot(x='running_time', y='runtime', kind='scatter')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Assumption\n",
    "# Create a function that fills missing data and drop redundant column.\n",
    "As shown in the data above:\n",
    "- As shown in the data above the running_time vs the runtime, it was observed that the runtimes are very close together with the Wiki data having outliers\n",
    "- Wikipedia data has more outliers in comparison to the Kaggle data\n",
    "- Some Kaggle movie have 0 runtime where Wiki has data.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x1f267481708>"
      ]
     },
     "execution_count": 105,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYMAAAESCAYAAAAfXrn0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjMsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+AADFEAAAgAElEQVR4nO3dfZzUdb3//8drZi9AQMCFCIQFDS9CAsz9aYTy9ap+HlPsHK+74NTP9NjJ0lOmeU5p2jn90s6pb2WWlJ6kPJpBCV6lmRZieLHQgoB9dRODBUVcAVmEvZh5ff+YmWV2LnZmduezM7vzvN9ue2PmM5/5zGsWmNe8r15vc3dERKSyhUodgIiIlJ6SgYiIKBmIiIiSgYiIoGQgIiIoGYiICIM4GZjZnWb2hpmtz+PcejN70sz+bGbrzOzMgYhRRGSwGLTJAPgZcEae534VuM/djwUuAm4LKigRkcFo0CYDd18BvJV8zMzeY2a/NbPVZvaUmR2dOB04OH57NLBtAEMVESl7VaUOoMgWAZe7+8tmdgKxFsCpwNeBx8zs88AI4PTShSgiUn6GTDIws5HAB4FfmVnicG38z4uBn7n7f5nZXODnZjbT3aMlCFVEpOwMmWRArMtrl7vPyfDYJcTHF9x9lZkNA8YBbwxgfCIiZWvQjhmkcve3gU1mdj6AxcyOP7wZOC1+/L3AMGBHSQIVESlDNlirlprZPcDJxL7hbwduAJ4AfgRMBKqBe939JjObAfwEGElsMPkad3+sFHGLiJSjQZsMRESkeIZMN5GIiPTdoBxAHjdunE+bNq3UYYiIDCqrV69+093HZ3psUCaDadOm0djYWOowREQGFTP7W7bH1E0kIiJKBiIiomQgIiIoGYiICEoGIiKCkoGIDGGtbe2s3bKL1rb2UodS9gbl1FIRkVyWNW3l2qXrqA6F6IxGueXcWSyYc2ipwypbahmIyJDT2tbOtUvXsb8zyp72LvZ3Rrlm6Tq1EHqhZCAiQ07Lzn1Uh3p+vFWHQrTs3FeiiMqfkoGIDDmTxw6nM9pz76rOaJTJY4eXKKLyp2QgIkNO3chabjl3FsOqQ4yqrWJYdYhbzp1F3cja3E+uUBpAFpEhacGcQ5k3fRwtO/cxeexwJYIclAxEZMiqG1mrJJAndROJiIiSgYiIKBmIiAhKBiIigpKBiIigZCAiIigZiIgISgYiIkLAycDMhpnZc2a21sw2mNmNGc75lJntMLOm+M9ngoxJRETSBb0CuR041d3bzKwaWGlmj7j7Mynn/dLdrwg4FhERySLQZODuDrTF71bHfzzI1xQRkcIFPmZgZmEzawLeAH7n7s9mOO1cM1tnZkvMbEqW61xmZo1m1rhjx45AYxYRqTSBJwN3j7j7HGAycLyZzUw55QFgmrvPAh4H7spynUXu3uDuDePHjw82aBGRCjNgs4ncfRfwB+CMlOOt7p7Yi+4nwHEDFZOIiMQEPZtovJmNid8eDpwO/CXlnIlJdxcALwYZk4iIpAt6NtFE4C4zCxNLPPe5+4NmdhPQ6O7LgS+Y2QKgC3gL+FTAMYmISAqLTfgZXBoaGryxsbHUYYiIDCpmttrdGzI9phXIIiKiZCAiIkoGIiKCkoGIiKBkICIiKBmIiAhKBiIigpKBiIigZCAiIigZiIgISgYiIoKSgYiIoGQgIiIoGYiICEoGIiKCkoGIiKBkICIiBL8H8jAze87M1prZBjO7McM5tWb2SzNrNrNnzWxakDGJDGWtbe2s3bKL1rb2Uocig0zQeyC3A6e6e5uZVQMrzewRd38m6ZxLgJ3uPt3MLgJuBi4MOC6RIWdZ01auXbqO6lCIzmiUW86dxYI5h5Y6LBkkAm0ZeExb/G51/Cd10+VzgLvit5cAp5mZBRmXyFDT2tbOtUvXsb8zyp72LvZ3Rrlm6Tq1ECRvgY8ZmFnYzJqAN4DfufuzKaccCmwBcPcuYDdQl+E6l5lZo5k17tixI+iwRQaVlp37qA71/O9cHQrRsnNfiSKSwSbwZODuEXefA0wGjjezmSmnZGoFpLYecPdF7t7g7g3jx48PIlSRQWvy2OF0RqM9jnVGo0weO7xEEclgM2Czidx9F/AH4IyUh1qAKQBmVgWMBt4aqLhEhoK6kbXccu4shlWHGFVbxbDqELecO4u6kbWlDk0GiUAHkM1sPNDp7rvMbDhwOrEB4mTLgX8EVgHnAU+4e1rLQER6t2DOocybPo6WnfuYPHa4EoEUJOjZRBOBu8wsTKwVcp+7P2hmNwGN7r4cuAP4uZk1E2sRXBRwTCJDVt3IWiUB6ZNAk4G7rwOOzXD8+qTb+4Hzg4xDRER6pxXIIiKiZCAiMlgEucI86DEDEREpgqBXmKtlICJS5gZihbmSgYhImRuIFeZKBiIiZW4gVpgrGYiIlLmBWGGuAWSRJK1t7VrBK2Up6BXmSgYicdoPQMpdkCvM1U0kgvYDEFEyEEH7AYgoGYig/QBElAxEGJjZGs3b97CkcQvN2/cU7Zq5BFm+QIYWDSCLxAU5W+P6+19g8TObu+8vnFvPTee8r2jXz0QD4lIItQxEktSNrGX2lDH9SgSp38abt+/pkQgAFq/aHGgLQQPiUii1DESKKNO38Y6uaMZzm7bsYvqEUYHEkRgQ38+B104MiGv9hGSiloFIkWT7Nj6t7qCM58+ZMiawWDQgLoUqKBmY2Ylm9un47fFmdliO86eY2ZNm9qKZbTCzKzOcc7KZ7TazpvjP9ZmuJRK0/g62ZpueWl0VZuHc+h7HF86t724VFHOQNzFIvXNvR+AD4jK05N1NZGY3AA3AUcB/A9XAL4B5vTytC/iSu68xs1HAajP7nbtvTDnvKXc/q7DQRYqnGIOtk8cOp629q8extvYuJo8dznFTD+He57ZgZrg7DVMPKdrrJmQapH762lNVXkPyUkjL4O+BBcBeAHffBvTa4enur7n7mvjtPcCLgKYzSFkp1mDrph1teMoxB5o27+TapevoiDjtXVE6Is41S9fRvH1P0QZ5sw1S79zb0e8BcakMhSSDDnd3Yv++MbMRhbyQmU0DjgWezfDwXDNba2aPmNkxWZ5/mZk1mlnjjh07CnlpkV4Va/XxipffzHj8sY3bM16/acuuoq16btqyK+Px5Wu3aQaR5KWQZHCfmd0OjDGzS4HHgZ/k80QzGwksBa5y97dTHl4DTHX32cAPgPszXcPdF7l7g7s3jB8/voCwRXpXrMHW+UeMy3j8wzMmZLz+nCljijbIm20w+o6VrzDv5idY3rS14GtKZck7Gbj7fwJLiH2oHwVc7+4/yPU8M6uOP+dud/91huu+7e5t8dsPA9Vmlvl/lUgAirX6uOGwOk6aXtfj2EnT6zhtxrszXn/6hFFFG+SdPmFU2iA1wN6OqNYYSF4s1vMT0MXNDLgLeMvdr8pyzruB7e7uZnY8sYQz1XsJrKGhwRsbGwOJWSpXsfYyaNzUyoqX32T+EeNoOOxAcsh2/WLuodC8fQ/L127jjpWvsLfjQKtjVG0Vv/jMCcwOcDqrlD8zW+3uDZkeyzmbyMz2QNq4GIAB7u4H9/L0ecAngRfMrCl+7F+BemJP/jFwHvBZM+sC9gEX9ZYIRIKSb634XB/eDYfV9UgCua5fzBr10yeM4h8/OI1FT73S47jWGEguOZOBu/d5iaS7rySWNHo751bg1r6+hshAGgz1fhLdXtekxKkZRdKbQtYZHJLh8B537yxiPCJlK3kKaqLMwzVL1zFv+riy+6ANeotEGXoKqU20BpgC7CT2bX8M8JqZvQFc6u6rA4hPpGwMtno/+XQ/ac9nSSgkGfwW+I27PwpgZh8GzgDuA24DTih+eCLlY6jV+xkMXV4ycApZZ9CQSAQA7v4YMN/dnwH0lUKGvIHYAGegqMS1pCqkZfCWmV0L3Bu/fyGw08zCQOYavSKDVPP2PTRt2cWcKWN6lJnua198uXXHDLYuLwleIcngY8ANxFYIG7AyfiwMXFD80ERKI9euZIVOBS3H7pih1uUl/VfICuQ33f3z7n6su89x9yvcfYe7d7h7c5BBigyUYu9KVq7dMUOpy0uKo5CppQ+QvvhsN9AI3O7u+4sZmMhAa21rZ/nabRkf6+uuZOXcHaPpp5KskG6iV4DxwD3x+xcC24EjiRWs+2RxQxMZOImunHCWJZJ93ZWs3Ltjirn6WQa3QpLBse4+P+n+A2a2wt3nm9mGYgcmMlCSu3IyuaBhMns7IrS2tRf8wanVwDJYFJIMxptZvbtvBjCzeiBRXbSj6JGJDJBMXTkH1YT4zImHM7K2iu88/hKPvPB6nwd/1R0jg0EhyeBLwEoz+yux2USHAf8c3+TmriCCExkImbpyog4LZk/irFtXFqX8hLpjpNwVMpvoYeAI4Kr4z1Hu/pC773X3/x1UgCLFlNgwPnl2UKIrp7bKOKg6TG2Vccu5s9jbESnaTmQi5a6QlgHEksFRwDBgVnxz78XFD0uk+K5Zspb7Glu67yevH4hNk7N4YfbYKHK5D/6KFFPeLQMzu4HYtpQ/AE4BbgEWBBSXSFEt+uNfeyQCOLB+IDGA3N4V5Z2OCO1dsbUAgObiS8UopGVwHjAb+LO7f9rMJgA/DSYskeJpbWvnlkf/kvGxpi27OGLCqKxrATT4K5WikGSwz92jZtZlZgcDbwCHBxSXSNG07NxHTThEVzR96uicKWMYO6Km1+4gDf5KJSikammjmY0htsBsNbH9DZ7r7QlmNsXMnjSzF81sg5ldmeEcM7Pvm1mzma0zs/cX9A6kIrW2tbN2y66sZR3Ov+0p3nPdQ5x/21NMHjs8YyXFc+ZMZG9HBEjvDvraWTNo2bkvsLIRyfHnei/5XEOkv6wv2w2b2TTgYHdfl+O8icBEd19jZqOIJZGPuvvGpHPOBD4PnElsT4TvuXuveyM0NDR4Y2NjwXHL0JCr8Nu0rzyU9pwvfehIbn3yZcJmdESinPm+iTy2cXuPayS6g9Zv3c03HtoYWGG55Pj3d0Vwd4ZXVxX0WuVY/E7Kn5mtdveGTI8VMoB8U+K2u78KbDCzu3t7jru/5u5r4rf3AC8Cqf9izwEWe8wzwJh4EhFJk6vw2/m3PZXxed99/CXA+OzJ0/ntlfN5bOP2tGtAbAbRNx7aGFhhudT4OyNOV5SCXqtci9/J4FZIN1G9mV0HYGa1wG+Al/N9crw1cSzwbMpDhwJbku63kJ4wMLPLzKzRzBp37NhRQNgylCRWCydLDPa2trWzevPbGZ8XdWjvivLDPzSzbff+jNfYsG03T/7lDcJmaY8Va21BpvgLfa3efgcifVXIAPKngbvjCeEU4BF3/24+TzSzkcBS4Cp3T/3fmqk0WFrflbsvAhZBrJuogLhlCMk293/91t1cuGhVzl2WYh+innaN/V0RLl3cSHU41D2OkHz9Yq0tyBR/oa+l9Q8ShJwtAzN7f3xQ91jge8Sqlb4M/DGfwV4zqyaWCO52919nOKUFmJJ0fzKQuY6wVLzUOvw1YfjIzHdz4wPrsxaaS9YZjXLMpNE9rlFbFcLdae9y2toPJIIRNeE+rS3obWA3Nf7qsFEVoqB1DNqLQIKQcwDZzJ7s5WF391N7ea4Rq1v0lrtfleWcjwBXcGAA+fvufnxvMWkAWVrb2vnq/et5ZP3rWc8JAdPqhrHt7Y6MA62JrSh37+vkc3evYU97V/dzR9SGufHsYzjl6HcFsqtZ8jaYQJ/WMZTbVppS/nobQM7ZTeTup+T5Iv/o7qkF6+YR2+fgBTNrih/7V6A+fu0fAw8TSwTNwDvEuqNEerVzb0eviWBYdYinrz2VupG1WT80E+sHWtva07pdIlEvOBEkD+zmKmyXunahLx/mWv8gxVRobaLeXElK9VJ3X0nmMYHkcxz4XBHjkCHu/jVbuP2pTRkfqw2HsBA9uk1yfWgWa8+Bct7VTCSXYiaDXj/0RYrhA9/8Ha+/nX37jP+6YDZz31NX8IdvMcpOaGBXBrNCppbmohk+Epjfb3ydC3/8p14TwcK59Zw1e1J310+hq3PrRtYye8qYPn+Lz3dgVyuHpRypZSBl7+RvP8Grrdnn0L934ih+cNGx3RvWl3J1bq4WhlYOS7kqZAXyYTmOPV2UiESSfPrO53pNBAD/dNJh3YmgHFbnZmthlENsItkU0k20NMOxJYkb7n5F/8MROeCynz3Lky/1vtp84sE1fPT9B5aptOzch0d79lh61Mtida5WDks5y9lNZGZHA8cAo83sH5IeOpjYjmciRZep2FyqMHDdmTN6HBtRE6Y90jMZtEecETXhYobXJxpglnKWT8vgKOAsYAxwdtLP+4FLgwtNKtXVv1yT13kRSOtm2dsRYVh1z3/Ww6rTS0yUglYOSznLZ9HZMmCZmc1191UDEJNUsN9vfJ37176W9/mp8/izfcvu77fvxMK1ETVh9nZE+jz9tLcBZq0ollIqZDZRq5n9Hpjg7jPNbBawwN3/PaDYpMJ8+Lt/4KXte3s9p7bKaO860A2U2s1SrAVkyRIzgAD2d0apDRsWsj7PBMq0CE6zjKTU8t7cxsz+CHwZuN3dj40fW+/uMwOMLyPVJhpabn/yZe5+djObd+3v9byqENy4YGZeG88U61t2a1s7825+ImMRvOSSF/2R6TWKdW2RZP2qTZTkIHd/znrWeu/KdrJIPo76t4doz7M7f3h1FTMPHc3T156a84O+WHV7MpWYSChWqQmVsZByUEgyeNPM3kN8pbGZnQfk37krkuLzd6/OOxHAgS6hgSzQ1tv+A8WaCaRZRlIOClln8DngduBoM9sKXAV8NpCoZMi7+pdreOCF7FVHIbaGoNQzb5JnACVmKdWGLe948tn4XrOMpBzkPWbQ/QSzEUAovqdxSWjMYHDLtYZg5qSR/MvpR3HajHeXzQybvswmKnTj+3J5rzJ0FWXMwMy+mHIfYDew2t2bMj5JJEnz9j1cs7T3fyq1YXjwC/+r+3651OwvNI5MexsA3RvoZNrnoFzeq1SmQsYMGuI/D8TvfwR4HrjczH7l7rcUOzgZOq6//wUWP7O513MWvO/dfP/jxw1QRMHqbeAZNEAs5aeQZFAHvN/d2wDM7AZitYnmA6sBJQNJ09rWzqq/tuZMBOcdO5H/vDDnltqDRjE2vhcZSIUMINcDycXkO4Gp7r4PyFh20czuNLM3zGx9lsdPNrPdZtYU/7m+gHhkgBVah39Z01aO+/fHueKeP+c897qPHJN27f7U/W/evocljVto3l6aoa1ibHwvMpAKaRn8D/CMmS2L3z8buCc+oLwxy3N+BtwKLO7luk+5+1kFxCElUOgK2da2dq68N/dQ0nnHTuSkoyYw7+Ynelzboc8rclO7pBbOreemc96X13OLKbX0BPRt43uRgVDQbCIzOw44kdhGNivdPeeUHjObBjyYaaWymZ0MXF1oMtBsooHVlxWyuWYMhUPGdy+Yzbzp49KuXVtlgNHeVfiK3Obtezj9uyvSjj/+L/O79zwQqVT9mk1kZock3d0U/+l+zN3f6md8c81sLbCNWGLYkCWOy4DLAOrr6/v5kpWt0CmMhayQ/e6jL/Kbtdt6vd6tFx/bvU/x2i270q4dtlDavnn5Drg2bdmV9biSgUh2+XQTrSa26tiIjRvsjN8eA2wG0nZAK8AaYuMObWZ2JnA/cESmE919EbAIYi2DfrxmRetLQbR8V8gecd1DdOb4mzHgrNmTer12xKPgPbNBvgOuc6aMKei4iMTkHEB298Pc/XDgUeBsdx/n7nXE9jj4dX9e3N3fTsxOcveHgWozG9efa0p2fd12MdcK2a/+ei1H/VvuRADQ+NXTc1772+fN5tvn9W1F7vQJo1g4t2fLceHc+l5bBdqgXqSwAeT/x90vT9xx90fM7Bv9eXEzezew3d3dzI4nlpxa+3NNya4/BdGy1eHPZ0eyhIVz6zO+TrZr97axfG+Om3oIv3y+BSPWpG2YekjWc1U6WiSm0EJ1XwV+Qez/2CfI8cFtZvcAJwPjzKwFuAGoBnD3HwPnAZ81sy5gH3CRF1ofQ/LW34JoqStkv/rrtQW9/n2NLVx52pEZP9gzrb7ty4rcROsnefA502rf5HOTVwlnO1dkqCskGVxM7MP8N/H7K+LHsnL3XI/fSmzqqQyAvm78kmnA+f41W/jFcy0FvX62Vki2Ae2+1OoppPWj0tEiB+SdDOKzhq4MMBYZAL1tu5hJajfKFz90JD94/CX2dGRfXTusCj55wlR+/tyWHlNGM7VCsnXT9LX7ppDWj0pHixxQyE5nTxLfyyCZu59a7KBy0TqDgdHa1s4Hv/VEjy6XfKz+6unUjaxledNWrv7VWsyMaDTKZ046nLnvGccxkw4GYMO2t7l0cWOP69dUhfifS47nE3c+1+edv5Y3bU1r/WRLJIWcKzLYFWuns6uTbg8DzkU7nQ1pdz+7ueBEcM6cid0f2I2vvkVHxEl8h/jRH1/hR398hZBByKAmHE67fkdXlIt++izhlOsW0n1TSOun0JaSyFBVSDfR6pRDT8f3RZYhqLWtnR8++XLBz/vt+u20trWzc29H1uJ0UY/9dEUzb3PWFfG0bxmFdt8UMvis0tEihe1nkDw/L0SsnPW7ix6RlIWWnfvi39wLa/yFQ0bLzn283M8CccOqQ0SjTm1VuF8D3aVQLnGIFKKQbqLESmSIdQ+9ClxS7ICkPEweO7x7I5ZCtHfGdgEbUZPa0ZNd2CAUMjojPYekHv7CSX3aVayUff/lEodIoQopYT0D+CGwFlgPPAJoFHeIunxx3/5qQ6FYGYmxI2oIhyzH2TFm8PUFx6StOJ4+YRSzp4zJq0XQl5XVxVYucYj0RSEtg7uAt4Hvx+9fDPwcOL/YQUlx5dNtkXzOl+5dw/ObMxd8S7hj4XE8s+ktFq/6W8/qolVhWnbuA+Cg6nCP1sXw6hCf+MBU/ufZzeztiCQdr2LmpNE8fe2pfepeKZf1AuUSh0hfFJIMjnL32Un3n4xXG5Uylk+3ReKcsFmPD+lshlWHuPzuNUSjTkrPTo+B3tQ5/A5c2DCF/356U4/j+zq7uhNAXz40y2W9QLnEIdIXhXQT/dnMPpC4Y2YnAE8XPyQpllzdFq1t7ax46Q2uWbKW/Z3RvBIBwP7OKJ2R9ERQW3WgoFy24nZjR9Rg1rP7KPV+oXIV0hso5RKHSF/ks5/BC8S+1FUDC81sc/z+VLLvcCZloLdui5XNb3Lt0nWEzGjvyr3w8L0TRtCyqz3roPJB1WF+/MnjmH/k+O5jmebwr92yi2FVYTojB66T6Frqz4dmuawXKJc4RAqVTzeRtqQcpLJ1W4yoCXe3GPLxwcPG8IOPNzDv5ieynhPFu1cWJ0vt+gmyK6Vc1guUSxwihchnP4O/9fYzEEEWS6XVrc/WbbG3I0J1KP8ewn84LrY/QK4N3oGcv191pYiUp4L2QC4XfalNVMnzv1NnE2XbJzibkbVhuqLOLefOyrrBe6LbKd/frxZmiQy83moTVUQy6MuG7kPV5+9ezQMvvN6n59ZWGT9Z2MAxk0anlZrW71ek/BWrUN2gpfnfMUf860PkGiYIWaxuUCbtXc7lv1hD1L3HN3/9fkUGv0Kmlg5amv8Nc7/5eM5E8K4RVVkTQcI7HZG0KaqZfr/tkWhBJSlEpLQCTQZmdqeZvWFm67M8bmb2fTNrNrN1Zvb+IOIo5aDlQA5ax9YN7GDFS2/QvH1P9+tO+8pDvPZ27tf/yadOoDacPue/Npz+zyRRkA56/n6HVcfONXfOunUli/74V5Y0bqG5n4XrRCRYQXcT/YzYtpaLszz+d8AR8Z8TgB/F/yy6Usz/HshB62VNW/nSfU0kbw9QGzbaU1eGZVA/tpYV155Oa1s7FjKSV5PVVoX4r/Nn86Vfre1RdmJve4T1W3cze8oYIPb7nTHxYM78/lMAsdeNON985C/dz1k4t56bznlff9+qiAQg0JaBu68A3urllHOAxR7zDDDGzCYGFU/dyNq8Cp8Vw0AWLWtta+eaJWtJ3Ycmn0Sw5J8+wA8+1kBrW3vGFtS3z5vF3PfU8f+dOC3tud94aGOP97O3I0JtVfauocWrNquFIFKmSj2AfCiwJel+S/zYa6knmtllwGUA9fX1AxJcfwzkoGrLzn2ELQTkV04ioTZsfOyO56gN92y5JLegVja/ybybnyCUoWRE6vvJNHaQqmnLLqZPGFVQnCISvFIPIGcqSpPx66y7L3L3BndvGD9+fKZTyspADlpPHjuciBe2PSXEWg4dXQdaLlcvWUfz9j3dLSigu3XzToa6RanvJ7llcVB15n9ac+LXFZHyUupk0AJMSbo/GdhWoliKqj+D1oUOOteNrOXb583OfWJcbVWImrB1D/YmdHRFOfP7T7G8aStwoHWT6qDqcNb3s2DOoTx97ancc9lcLmiY3OOxhXPr1SoQKVOl7iZaDlxhZvcSGzje7e5pXUSDVT6D1qkrcfsy6Nza1s4X7m3KK6awwX98dCZzpozhrFtXpj3eEXGuWbqOedPHZWzd1ISNW+LjCNkSW6I2z+wpY7jspMNp2rKLOVPGKBGIlLGgp5beA6wCjjKzFjO7xMwuN7PL46c8DLwCNAM/Af45yHiyCXL6Z2+D1suatjLv5if4xE+fZd7NT3D3s38reNB5WdNWjvv3x/OOJ+Iwre4gpk8YxS3nzqKmKv2fQPJYQNqUUeDqJWt5uvnNvF5v+oRRnNcwRYlApMwF2jJw94tzPO7A54KMIZdS1SxKnm2UGGS+8YGNVKdsFdnboPPvN77OlXm2CJK92voODYfVMW/6OL5z/iz+5b4mOpOGBJLHArJNGU20HrTCWGRoKHU30YBK7ZLJ9IE8UB9yGWcbhY3OrvwGnU/99pO80vpOn157zpQxPZIgGFUhZ3h1VXdCTH7/iSmjHUl7EKjchMjQUjHJIFMLYGrdiAGZ/tna1s6GbbsB45hJB1M3sjZjf3wk6txw9jF846GNhCzWf//FDx3ZI5ZpX3ko79e9Y+FxXLJ4ddrxXe90pCXB2qoQP/z4+7vjS6ZyHiJDX6lnEw2IbAvARtSEA/+QW9a0lQ/8/79n4Z3Ps/DO5zjhm4+zvGlrd398bZVxUHWY2irjlnNn8W/6LMcAABLdSURBVPEPTGXB7Em80xGlK+J88+G/cP2yF4DCEgHAZb9Yk/H4ipffTJslVBMOMXp4dcYkqD0IRIa+imgZZFsAtrcjwi3nzuKalBZDsT7kYiuD19GZtBK4KwpfXrKWedPHxRdUWGxU1mNjBc3b93BfY0uP6yxetZnFqzYX/PqRLFXnZk8eXXAS1HaOIkNbRSSD3ro5Zk8ZU9QPueRxiZad+wiH0tfVhS3Ehm1vc+3SdT3q/VyzdB1fOePofr1+LtVhY9yoYX1KgtrOUWToqohkkOjmyPbhV6wPudRxia99ZAadkfSVwbHVwpm/tY8L+MM2HLJAkqCIDG4VkQwg+G6OTDOTbnpwQ8aumuvPPoZJo4enbUi/vzNKV6Sw+kK5GFBTFaImHFwSFJHBr2KSQVAS3UK793WmjUsYRjTDtqJTxg6PTddMKTFdGzZWvdJbkdfCXf6/DmfqIQfRvGMvZxwzgYbD6tJiD7JloL2ORQaHikkGQSwuS75mRyTao/8fYH9qTelusa6ajpQS0x0RZ+7hh/DLlAHkvjJg0YpNROIJ6acrN3XvKTAQi+1KtaBPRApX0VNLCyk/kVqyIvWaqYkgIfUXXBWCYyYdzM69HWmjBg5cdd+6/N9YDrF9anq+yuJVm2nc1Br4XgsDuZ+DiPRfRSSDTNU3E4vL8pFaQ2h509asFT1TXXx8fY+1BN+5YA51I2tp2rKrT+8l1cxJB2c8Xh22jDOZIPM6g0J+H/no7+9cRAZWRXQT9WcFbbaSFQ9ecSIdGWYKpfr0vGl88cNHpvWbT6s7qA/vJN1H50xi/ba3045bbPFCxufMP2Ici556pcexYi+206plkcGlIloGB1b7hjioJkxtVf4raDN9ww2bsbcjwhWnTO/1uefMmcjejgg793akPVZdFc64s08hjFidodOP7rnZT9iMq//fIzn/uClpf8EXNEymuirM186aEeiKYq1aFhlcKqJlAInvyB5f6Zt7b+CETN9w93ZEWL9tNx87oZ5bn3yZ9q4D1wsBoRCEzFjW9BoPNL1GlFjtHwduOHsGHz9hKrc98VIBUWRmwHm3P9PjWHXYustYJMyfXsep751AR1eU7zz+Eo+88Hr3OoiZh44ObKaPVi2LDB7mGaY+lruGhgZvbGzM+/zWtnbm3fxEj3n9w6pDPH3tqXl9QN39zN/4t/vX9ziWeP7TzW/y5SVrCVuIrmgEx3qUnygXS/7pA3zizuf6/DsQkcHPzFa7e0Omxyqim6hl5z48ZfGXRz3vwcyZh45mZG24x7HEYGiP+kJY2f5CB2LQWEQGr3L97CqqETXhHou7ILZJy4iacJZnHNDa1s7ufZ1p3/Y7o1FG1IS76wu90xGhI+Jpr1Mu5h8xTgO6IpJV4MnAzM4ws/9jZs1m9pUMj3/KzHaYWVP85zPFjmFvRyRt8/dh1bGqpdm0trXz/d+/zAe/9Xs+d/caItEo1WHrMRi6tyNCVcr0zdT7QarO8LdXEw6RGsLCufU0HFanAV0RySrQAWQzCwM/BD4EtADPm9lyd9+Ycuov3f2KoOKYPHY4HSmLwjq6sn8rXta0lWuWHKgo2t4V2+Grtgp++PFjOWbSaOpG1nL3M3+jrb1nQunKUja62E47ejxPNbcyoio2RjH/iDpWvLyDqpBhZnzpQ0dxyIiaHhvRa0BXRLIJumVwPNDs7q+4ewdwL3BOwK+ZZufeDlI/o6NOximfiXUFmVYUmxmjh9d0b5n5jYdSc9rACBusbG6loyvK3o4IHZEoj/9lBx0ReKczQnuX853HX+KUo9+VthF93chaZk8Zo0QgIj0EnQwOBbYk3W+JH0t1rpmtM7MlZjYl04XM7DIzazSzxh07dhQURLbVvpmO97ayeH9ntHucYcO2twn1e6VA33x0ziRqwr3/1WlwWEQKEXQyyPRpmdqP8gAwzd1nAY8Dd2W6kLsvcvcGd28YP358plOymjNlTN7HM60rSKgNxxabLWvayqWLG3mns7jlpvNRHTY+e/L0rDEmaHBYRAoRdDJoAZK/6U8GtiWf4O6t7p6oXvYT4LhiBzF9wigWzq3vcWzh3Pq0LhSIdaN87awZ1ITT85iFrMcMolL4+oJjmD5hVNpg8MK59RocFpE+C3oF8vPAEWZ2GLAVuAj4WPIJZjbR3V+L310AvBhEIK/s2Nvj/qaU+wnLmrbyjQc3Uh0O0RmJ9GjGXNAwmb0dkbR9CwbKiJowMyeNBjIPBl95WnoNJBGRfASaDNy9y8yuAB4FwsCd7r7BzG4CGt19OfAFM1sAdAFvAZ8qdhyNm1pZ2dza49hTza00bmpN2+wlUZQuk3ue28Lx0+p4p6Or2CFmVBWC5AZIxL1H10/qTmXauUxE+irw2kTu/jDwcMqx65NuXwdcF2QMj258Pevx5GSQGDzO9q2/M+Jcde+fGah1ZZeedDj//adX45vnRPjcyb0XxhMR6auKWIF8+LiRGY/XhEM9NluZPHY4+zp7/9bfNUCJoCoEnznpcJ6+9lQunX84YCxa8Ur3fgoiIsVUEcngXaMyd538ZMUmPvit3/f4cDUrzXRRiCWA1E1wAG77QzPtXdoxTESCUxElrJ/Z1JrxeEfUIQpfvK+JGRMPpmnLLmqrYgPHA+2zJx/OZ048PG0AuGXnvrQSF4k1BBofEJFiqYhksH3X/l4f74rCGd9bQW1VuNd6RUG6c+UmPnPi4cxOWfuwfuvutJIXyWsIWtvaNYNIRPqtIpLBlt25V+J2RaGrRIkAoCYcTvu2n63kxdfOmkHdyFqWNW3l2qXrqA6F6IxGueXcWSyYk2mBt4hI7ypizOCM904odQg5ZVoxnKk0RmKtQfI0WI0liEh/VUQy2Fei1cL5yrYnc6bSGIm1BpkSheoRiUhfVUQ30bOb3sr73MTHa9DpY1RtFR2RCFeccgQfO6E+Y39/YlP5a1K6ghLnarMaESmWikgG7zt0NKteSU8IRnrVvKCTQE04xMNfOJG9HZG8Bn2z7UGQK1GIiBSiIpLB5jcz1yEKev1YOASRlOzy+VOnZyyQ15tsZSa0WY2IFEtFJIPnN+ffTVQsNeEQZk4kaVed2irjYyfU9/KswqkekYgUQ0UkAyvBHvU3LJjBqNoqdeOIyKBQEclg9/6BqTKaUBM2Zk4azewpY9SNIyKDQkUkg8AHB1KYWfesHnXjiMhgUBHrDDoHOBlcf/YMJQARGVQqIhkEJQTUhnseS96NTERksFAy6KOQwTf+fiaWsgo4dTeyoLW2tbN2yy6VoRCRfgl8zMDMzgC+R2zby5+6+7dSHq8FFgPHAa3Ahe7+atBx9VfU4d9+sz7t+MiaEKf/55NMHXcQsw8dywvbdvNOexe11SF27uvilCPHM//I8axt2c38I8bx6PrXeHD965w1891cePxUmrbsYs6UMex6p4NHN27n8HEjOOJdI3m19R3mxCuaJs7Z8NrbPQrVfe0jM5h56OjuZJQYuN65t6P7OYk1DoOt2ulgi7dU9HuSvjL34DrUzSwMvAR8CGgBngcudveNSef8MzDL3S83s4uAv3f3C3u7bkNDgzc2NuYdx7SvPNSX8MteyGJJKdnI2jDtXVHcneHVVezt6OpxzsK59Rw39ZBBVe1U1Vnzo9+T5GJmq929IdNjQXcTHQ80u/sr7t4B3Auck3LOOcBd8dtLgNOslNuNDSKpiQCgrT1CZ8TpisKe9q60cxav2syXf9U0aKqdqjprfvR7kv4KOhkcCmxJut8SP5bxHHfvAnYDdSnnYGaXmVmjmTXu2LEjoHArgzF4qp2qOmt+9HuS/go6GWT6hp/6fTafc3D3Re7e4O4N48ePL0pwQ0FN2BhRE859YhJn8FQ7zVTGu5zjLRX9nqS/gk4GLcCUpPuTgW3ZzjGzKmA0UNRiQq9+6yPFvFzZWDi3nlXXncb/XPoB/uPvZzKsOsSo2iqqw0ZVKFYmO2X7ZBbOrec/z5/Tfe6w6sx7KZSLRHXWwRJvqej3JP0V9AByFbEB5NOArcQGkD/m7huSzvkc8L6kAeR/cPcLertuoQPICUENJNeGoD0K40ZUMWpYNbv2dgzIbKLU6qfJM0lAs4kqkX5P0pveBpADTQbxFz8T+N/Eppbe6e7/YWY3AY3uvtzMhgE/B44l1iK4yN1f6e2afU0GIiKVrLdkEPg6A3d/GHg45dj1Sbf3A+cHHYeIiGSnFcgiIqJkICIiSgYiIoKSgYiIMACziYJgZjuAv/Xx6eOAN4sYzmBRie+7Et8zVOb7rsT3DIW/76nunnHV7qBMBv1hZo3ZplYNZZX4vivxPUNlvu9KfM9Q3PetbiIREVEyEBGRykwGi0odQIlU4vuuxPcMlfm+K/E9QxHfd8WNGYiISLpKbBmIiEgKJQMREamsZGBmZ5jZ/zGzZjP7SqnjGQhmdqeZvWFm60sdy0Axsylm9qSZvWhmG8zsylLHFDQzG2Zmz5nZ2vh7vrHUMQ0UMwub2Z/N7MFSxzJQzOxVM3vBzJrMrCglnCtmzMDMwsT2VvgQsQ11ngcudveNJQ0sYGY2H2gDFrv7zFLHMxDMbCIw0d3XmNkoYDXw0aH8dx3fN3yEu7eZWTWwErjS3Z8pcWiBM7MvAg3Awe5+VqnjGQhm9irQ4O5FW2hXSS2D44Fmd3/F3TuAe4FzShxT4Nx9BUXeOa7cuftr7r4mfnsP8CLpe28PKR7TFr9bHf8Z8t/0zGwy8BHgp6WOZbCrpGRwKLAl6X4LQ/wDQsDMphHbOOnZ0kYSvHh3SRPwBvA7dx/y75nYxlnXQMrG3kOfA4+Z2Wozu6wYF6ykZGAZjg35b06VzMxGAkuBq9z97VLHEzR3j7j7HGJ7jR9vZkO6W9DMzgLecPfVpY6lBOa5+/uBvwM+F+8O7pdKSgYtwJSk+5OBbSWKRQIW7zdfCtzt7r8udTwDyd13AX8AzihxKEGbByyI95/fC5xqZr8obUgDw923xf98A/gNsW7wfqmkZPA8cISZHWZmNcBFwPISxyQBiA+m3gG86O7fKXU8A8HMxpvZmPjt4cDpwF9KG1Ww3P06d5/s7tOI/X9+wt0/UeKwAmdmI+ITIzCzEcCHgX7PFqyYZODuXcAVwKPEBhTvc/cNpY0qeGZ2D7AKOMrMWszsklLHNADmAZ8k9k2xKf5zZqmDCthE4EkzW0fsi8/v3L1iplpWmAnASjNbCzwHPOTuv+3vRStmaqmIiGRXMS0DERHJTslARESUDERERMlARERQMhARKXuFFJw0s/p4ocY/m9m6fGfSKRmIiJS/n5H/IsKvEps6fyyx9Re35fMkJQMZssxsWn9Kd8fLBI/r43M/amYz+vra8WtcbmYL47f/YGYNGc55OLHYTIauTAUnzew9ZvbbeH2ip8zs6MTpwMHx26PJs9JCVdGiFZFkHwUeBPpcNtvdf5zHOUN9MZ1ktwi43N1fNrMTiLUATgW+TqyI3eeBEcRWo+ekloEMdVVmdle873SJmR2U/I3fzBrM7A/x23Vm9li8r/V2koobmtnXzOwvZvY7M7vHzK6OH0/7dmZmHwQWAN+Or35+T2pQZvYuM1sdvz3bzNzM6uP3/xqP8+uJ10l6Xij+fv49fr/PrRcZvOJFGD8I/CpeqfZ2YqvQAS4Gfubuk4EzgZ+bWc7PeiUDGeqOAha5+yzgbeCfezn3BmBlvK91OZD4cG4AziVWCvsfiG2kkrAI+Ly7HwdcDdzm7n+KP//L7j7H3f+a+kLxAmPDzOxg4CSgETjJzKYSq8T5Tob4qoC7gZfc/at5/wZkKAoBu+L/vhI/740/dglwH4C7rwKGATm/MCgZyFC3xd2fjt/+BXBiL+fOj5+Duz8E7IwfPxFY5u774pvlPAA5v53l40/E6ijNB74Z//Mk4Kks598OrHf3/yjgNWQIipdk32Rm50OsOKOZzY4/vBk4LX78vcSSwY5c11QykKEutfiWA10c+Lc/LMf5kHkvDOj921k+niL24T8VWAbMJpZ4VmQ5/0/AKWaWGrMMcVkKTn4cuCResG4DB3Zu/BJwafz4PcCnPI8idEoGMtTVm9nc+O2Lie0N/CpwXPzYuUnnriD2Hwwz+ztgbPz4SuBsi206P5LYNou5vp3tAUbliG0F8AngZXePEpstcibwdJbz7wAeJtYS0eSPCuLuF7v7RHevjpftvsPdN7n7Ge4+291nuPtN8XM3uvu8+PE57v5YPq+hZCBD3YvAP8ZLOx8C/Ai4EfiemT0FRJLOvRGYb2ZriNWI3wzg7s8TGwNYC/yaWP/+7vhzsn07uxf4cnwwOm0AOX7dV+M3Ey2BlcRaGjsznR9/zneANeQ5KCiSL5WwFsmDmY109zYzO4jYh/dl7r6m1HGJFIuamiL5WRRfRDYMuEuJQIYatQxEAmZmPyQ2ayjZ99z9v0sRj0gmSgYiIqIBZBERUTIQERGUDEREBCUDEREB/i9UfmaSRZfItQAAAABJRU5ErkJggg==\n",
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
    "movies_df.fillna(0).plot(x='budget_wiki',y='budget_kaggle', kind='scatter')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Assumption\n",
    "As shown in the data above:\n",
    "- The budget_wiki data  have more outliers compared to the budget_kaggle data. \n",
    "- There are movies with no data in the Kaggle column, and wiki has budget data. "
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
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
