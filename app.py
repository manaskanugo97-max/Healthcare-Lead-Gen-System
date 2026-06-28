{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNEcTc7SGOcoy34X2tszRgA",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/manaskanugo97-max/Healthcare-Lead-Gen-System/blob/main/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pO8M6dNzDVt5",
        "outputId": "3cace524-633c-49df-983e-7ce312c9471b"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mounted at /content/drive\n"
          ]
        }
      ],
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%cd /content/drive/MyDrive/healthcare_lead_gen_project"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "T__cMgsEDrgh",
        "outputId": "9554fa8d-3667-4c4a-c63c-7f265bf676bb"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/drive/MyDrive/healthcare_lead_gen_project\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "print(os.listdir())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "i-16f615DzId",
        "outputId": "cde41442-26bc-4d8a-b917-478dc09bb216"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['data', '__pycache__', 'osm_scraper.py', 'online_presence_checker.py', 'website_analyzer.py', 'scorer.py', 'contact_extractor.py', 'merge_final.py', 'app.py', 'app_backup.py', 'config_colab_backup.py', 'config.py']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "import pandas as pd\n",
        "from config import FINAL_CSV\n",
        "\n",
        "print(\"Dashboard input file:\")\n",
        "print(FINAL_CSV)\n",
        "\n",
        "print(\"\\nFinal CSV exists:\")\n",
        "print(os.path.exists(FINAL_CSV))\n",
        "\n",
        "df = pd.read_csv(FINAL_CSV)\n",
        "\n",
        "print(\"\\nTotal rows:\", len(df))\n",
        "print(\"\\nColumns:\")\n",
        "print(df.columns.tolist())\n",
        "\n",
        "df.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 958
        },
        "id": "pkRgANXcEXLx",
        "outputId": "0902114f-a98e-43c1-8e70-13a93f83968e"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Dashboard input file:\n",
            "/content/drive/MyDrive/healthcare_lead_gen_project/data/healthcare_leads_final.csv\n",
            "\n",
            "Final CSV exists:\n",
            "True\n",
            "\n",
            "Total rows: 100\n",
            "\n",
            "Columns:\n",
            "['Business Name', 'Industry Category', 'Business Description', 'Location', 'Google Maps Profile Link', 'OpenStreetMap Link', 'Website URL', 'Website Classification', 'Website Status Code', 'HTTPS Used', 'Contact Page Found', 'Services Page Found', 'Website Analysis Reason', 'Online Presence Type', 'Referral Platform Links', 'Phone Number', 'Email Address', 'Owner / Founder Name', 'LinkedIn Profile', 'Lead Score', 'Business Potential Category', 'Reason for Classification', 'Detailed Score Reason', 'Source', 'Scrape Status', 'Created Date']\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "          Business Name Industry Category              Business Description  \\\n",
              "0      Centre For Sight            clinic    Clinic listed on OpenStreetMap   \n",
              "1  Dr. Vrinda Vashistha            clinic    Clinic listed on OpenStreetMap   \n",
              "2    Well Care Pharmacy          pharmacy  Pharmacy listed on OpenStreetMap   \n",
              "3  Rashmi Dental Clinic           dentist   Dentist listed on OpenStreetMap   \n",
              "4       Dr. A. R. pawar            clinic    Clinic listed on OpenStreetMap   \n",
              "\n",
              "                                            Location  \\\n",
              "0  Block no. 124 Section AB, Scheme No. 54, Vijay...   \n",
              "1  2-BB, Slice No.-5, Scheme No.-78, Vijay Nagar,...   \n",
              "2  EB 303, Scheme No 94, Bombay Hospital Square, ...   \n",
              "3          GH-28, Scheme No. 54, Vijay Nagar, Indore   \n",
              "4             AD 335, scheme 74c,vijay nagar, indore   \n",
              "\n",
              "                            Google Maps Profile Link  \\\n",
              "0  https://www.google.com/maps/search/?api=1&quer...   \n",
              "1  https://www.google.com/maps/search/?api=1&quer...   \n",
              "2  https://www.google.com/maps/search/?api=1&quer...   \n",
              "3  https://www.google.com/maps/search/?api=1&quer...   \n",
              "4  https://www.google.com/maps/search/?api=1&quer...   \n",
              "\n",
              "                              OpenStreetMap Link Website URL  \\\n",
              "0  https://www.openstreetmap.org/node/6187452264         NaN   \n",
              "1  https://www.openstreetmap.org/node/6187436057         NaN   \n",
              "2  https://www.openstreetmap.org/node/6187441510         NaN   \n",
              "3  https://www.openstreetmap.org/node/6187438667         NaN   \n",
              "4  https://www.openstreetmap.org/node/6187446196         NaN   \n",
              "\n",
              "  Website Classification  Website Status Code  HTTPS Used  ...  Email Address  \\\n",
              "0           Poor Website                  NaN         NaN  ...            NaN   \n",
              "1           Poor Website                  NaN         NaN  ...            NaN   \n",
              "2           Poor Website                  NaN         NaN  ...            NaN   \n",
              "3           Poor Website                  NaN         NaN  ...            NaN   \n",
              "4           Poor Website                  NaN         NaN  ...            NaN   \n",
              "\n",
              "   Owner / Founder Name  LinkedIn Profile Lead Score  \\\n",
              "0                   NaN               NaN         65   \n",
              "1                   NaN               NaN         65   \n",
              "2                   NaN               NaN         65   \n",
              "3                   NaN               NaN         65   \n",
              "4                   NaN               NaN         65   \n",
              "\n",
              "  Business Potential Category  \\\n",
              "0                        High   \n",
              "1                        High   \n",
              "2                        High   \n",
              "3                        High   \n",
              "4                        High   \n",
              "\n",
              "                           Reason for Classification  \\\n",
              "0  Business has an online presence but lacks a st...   \n",
              "1  Business has an online presence but lacks a st...   \n",
              "2  Business has an online presence but lacks a st...   \n",
              "3  Business has an online presence but lacks a st...   \n",
              "4  Business has an online presence but lacks a st...   \n",
              "\n",
              "                               Detailed Score Reason         Source  \\\n",
              "0  Website exists but digital quality is weak; Bu...  OpenStreetMap   \n",
              "1  Website exists but digital quality is weak; Bu...  OpenStreetMap   \n",
              "2  Website exists but digital quality is weak; Bu...  OpenStreetMap   \n",
              "3  Website exists but digital quality is weak; Bu...  OpenStreetMap   \n",
              "4  Website exists but digital quality is weak; Bu...  OpenStreetMap   \n",
              "\n",
              "  Scrape Status  Created Date  \n",
              "0     Completed    2026-06-27  \n",
              "1     Completed    2026-06-27  \n",
              "2     Completed    2026-06-27  \n",
              "3     Completed    2026-06-27  \n",
              "4     Completed    2026-06-27  \n",
              "\n",
              "[5 rows x 26 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-4fe8d8dd-4470-4065-8d13-db7e2a3b131e\" class=\"colab-df-container\">\n",
              "    <div>\n",
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
              "      <th>Business Name</th>\n",
              "      <th>Industry Category</th>\n",
              "      <th>Business Description</th>\n",
              "      <th>Location</th>\n",
              "      <th>Google Maps Profile Link</th>\n",
              "      <th>OpenStreetMap Link</th>\n",
              "      <th>Website URL</th>\n",
              "      <th>Website Classification</th>\n",
              "      <th>Website Status Code</th>\n",
              "      <th>HTTPS Used</th>\n",
              "      <th>...</th>\n",
              "      <th>Email Address</th>\n",
              "      <th>Owner / Founder Name</th>\n",
              "      <th>LinkedIn Profile</th>\n",
              "      <th>Lead Score</th>\n",
              "      <th>Business Potential Category</th>\n",
              "      <th>Reason for Classification</th>\n",
              "      <th>Detailed Score Reason</th>\n",
              "      <th>Source</th>\n",
              "      <th>Scrape Status</th>\n",
              "      <th>Created Date</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Centre For Sight</td>\n",
              "      <td>clinic</td>\n",
              "      <td>Clinic listed on OpenStreetMap</td>\n",
              "      <td>Block no. 124 Section AB, Scheme No. 54, Vijay...</td>\n",
              "      <td>https://www.google.com/maps/search/?api=1&amp;quer...</td>\n",
              "      <td>https://www.openstreetmap.org/node/6187452264</td>\n",
              "      <td>NaN</td>\n",
              "      <td>Poor Website</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>...</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>65</td>\n",
              "      <td>High</td>\n",
              "      <td>Business has an online presence but lacks a st...</td>\n",
              "      <td>Website exists but digital quality is weak; Bu...</td>\n",
              "      <td>OpenStreetMap</td>\n",
              "      <td>Completed</td>\n",
              "      <td>2026-06-27</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Dr. Vrinda Vashistha</td>\n",
              "      <td>clinic</td>\n",
              "      <td>Clinic listed on OpenStreetMap</td>\n",
              "      <td>2-BB, Slice No.-5, Scheme No.-78, Vijay Nagar,...</td>\n",
              "      <td>https://www.google.com/maps/search/?api=1&amp;quer...</td>\n",
              "      <td>https://www.openstreetmap.org/node/6187436057</td>\n",
              "      <td>NaN</td>\n",
              "      <td>Poor Website</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>...</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>65</td>\n",
              "      <td>High</td>\n",
              "      <td>Business has an online presence but lacks a st...</td>\n",
              "      <td>Website exists but digital quality is weak; Bu...</td>\n",
              "      <td>OpenStreetMap</td>\n",
              "      <td>Completed</td>\n",
              "      <td>2026-06-27</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Well Care Pharmacy</td>\n",
              "      <td>pharmacy</td>\n",
              "      <td>Pharmacy listed on OpenStreetMap</td>\n",
              "      <td>EB 303, Scheme No 94, Bombay Hospital Square, ...</td>\n",
              "      <td>https://www.google.com/maps/search/?api=1&amp;quer...</td>\n",
              "      <td>https://www.openstreetmap.org/node/6187441510</td>\n",
              "      <td>NaN</td>\n",
              "      <td>Poor Website</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>...</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>65</td>\n",
              "      <td>High</td>\n",
              "      <td>Business has an online presence but lacks a st...</td>\n",
              "      <td>Website exists but digital quality is weak; Bu...</td>\n",
              "      <td>OpenStreetMap</td>\n",
              "      <td>Completed</td>\n",
              "      <td>2026-06-27</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Rashmi Dental Clinic</td>\n",
              "      <td>dentist</td>\n",
              "      <td>Dentist listed on OpenStreetMap</td>\n",
              "      <td>GH-28, Scheme No. 54, Vijay Nagar, Indore</td>\n",
              "      <td>https://www.google.com/maps/search/?api=1&amp;quer...</td>\n",
              "      <td>https://www.openstreetmap.org/node/6187438667</td>\n",
              "      <td>NaN</td>\n",
              "      <td>Poor Website</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>...</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>65</td>\n",
              "      <td>High</td>\n",
              "      <td>Business has an online presence but lacks a st...</td>\n",
              "      <td>Website exists but digital quality is weak; Bu...</td>\n",
              "      <td>OpenStreetMap</td>\n",
              "      <td>Completed</td>\n",
              "      <td>2026-06-27</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Dr. A. R. pawar</td>\n",
              "      <td>clinic</td>\n",
              "      <td>Clinic listed on OpenStreetMap</td>\n",
              "      <td>AD 335, scheme 74c,vijay nagar, indore</td>\n",
              "      <td>https://www.google.com/maps/search/?api=1&amp;quer...</td>\n",
              "      <td>https://www.openstreetmap.org/node/6187446196</td>\n",
              "      <td>NaN</td>\n",
              "      <td>Poor Website</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>...</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>65</td>\n",
              "      <td>High</td>\n",
              "      <td>Business has an online presence but lacks a st...</td>\n",
              "      <td>Website exists but digital quality is weak; Bu...</td>\n",
              "      <td>OpenStreetMap</td>\n",
              "      <td>Completed</td>\n",
              "      <td>2026-06-27</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>5 rows × 26 columns</p>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-4fe8d8dd-4470-4065-8d13-db7e2a3b131e')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-4fe8d8dd-4470-4065-8d13-db7e2a3b131e button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-4fe8d8dd-4470-4065-8d13-db7e2a3b131e');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "df"
            }
          },
          "metadata": {},
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 14,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "40Q9882N94_J",
        "outputId": "93eb8bf2-da89-40f2-8048-a21371406bcd"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m9.2/9.2 MB\u001b[0m \u001b[31m52.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m11.3/11.3 MB\u001b[0m \u001b[31m78.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h"
          ]
        }
      ],
      "source": [
        "!pip install streamlit pandas -q"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%%writefile app.py\n",
        "\n",
        "import streamlit as st\n",
        "import pandas as pd\n",
        "import os\n",
        "\n",
        "from config import FINAL_CSV\n",
        "\n",
        "st.set_page_config(\n",
        "    page_title=\"Healthcare Leads\",\n",
        "    page_icon=\"🏥\",\n",
        "    layout=\"wide\"\n",
        ")\n",
        "\n",
        "def load_data():\n",
        "    if not os.path.exists(FINAL_CSV):\n",
        "        st.error(\"Final CSV file not found.\")\n",
        "        st.stop()\n",
        "\n",
        "    df = pd.read_csv(FINAL_CSV)\n",
        "\n",
        "    if \"Lead Score\" in df.columns:\n",
        "        df[\"Lead Score\"] = pd.to_numeric(df[\"Lead Score\"], errors=\"coerce\").fillna(0)\n",
        "\n",
        "    return df\n",
        "\n",
        "df = load_data()\n",
        "\n",
        "st.title(\"🏥 Healthcare Leads Dashboard\")\n",
        "st.write(\"Healthcare lead generation dashboard for clinics, hospitals, pharmacies, dentists, and healthcare centers.\")\n",
        "\n",
        "col1, col2, col3, col4 = st.columns(4)\n",
        "\n",
        "total_leads = len(df)\n",
        "high_leads = len(df[df[\"Business Potential Category\"] == \"High\"]) if \"Business Potential Category\" in df.columns else 0\n",
        "with_website = len(df[df[\"Website Classification\"].isin([\"Good Website\", \"Poor Website\"])]) if \"Website Classification\" in df.columns else 0\n",
        "with_phone = len(df[df[\"Phone Number\"].fillna(\"\").astype(str).str.strip() != \"\"]) if \"Phone Number\" in df.columns else 0\n",
        "\n",
        "col1.metric(\"Total Leads\", total_leads)\n",
        "col2.metric(\"High Potential\", high_leads)\n",
        "col3.metric(\"With Website\", with_website)\n",
        "col4.metric(\"With Phone\", with_phone)\n",
        "\n",
        "st.divider()\n",
        "\n",
        "search_text = st.text_input(\"Search business or location\")\n",
        "\n",
        "filtered_df = df.copy()\n",
        "\n",
        "if search_text:\n",
        "    search_lower = search_text.lower()\n",
        "\n",
        "    business_col = filtered_df[\"Business Name\"].fillna(\"\").astype(str).str.lower()\n",
        "    location_col = filtered_df[\"Location\"].fillna(\"\").astype(str).str.lower()\n",
        "\n",
        "    filtered_df = filtered_df[\n",
        "        business_col.str.contains(search_lower, na=False) |\n",
        "        location_col.str.contains(search_lower, na=False)\n",
        "    ]\n",
        "\n",
        "if \"Industry Category\" in filtered_df.columns:\n",
        "    categories = [\"All\"] + sorted(filtered_df[\"Industry Category\"].dropna().astype(str).unique().tolist())\n",
        "    selected_category = st.selectbox(\"Category\", categories)\n",
        "\n",
        "    if selected_category != \"All\":\n",
        "        filtered_df = filtered_df[filtered_df[\"Industry Category\"].astype(str) == selected_category]\n",
        "\n",
        "if \"Lead Score\" in filtered_df.columns:\n",
        "    filtered_df = filtered_df.sort_values(\"Lead Score\", ascending=False)\n",
        "\n",
        "st.subheader(\"Lead Results\")\n",
        "st.write(f\"Showing {len(filtered_df)} leads\")\n",
        "\n",
        "display_columns = [\n",
        "    \"Business Name\",\n",
        "    \"Lead Score\",\n",
        "    \"Industry Category\",\n",
        "    \"Location\",\n",
        "    \"Phone Number\",\n",
        "    \"Website Classification\",\n",
        "    \"Business Potential Category\",\n",
        "    \"Website URL\",\n",
        "    \"Google Maps Profile Link\",\n",
        "    \"Reason for Classification\"\n",
        "]\n",
        "\n",
        "available_columns = [col for col in display_columns if col in filtered_df.columns]\n",
        "\n",
        "st.dataframe(\n",
        "    filtered_df[available_columns],\n",
        "    use_container_width=True,\n",
        "    height=500\n",
        ")\n",
        "\n",
        "csv_data = filtered_df.to_csv(index=False).encode(\"utf-8-sig\")\n",
        "\n",
        "st.download_button(\n",
        "    \"Download Filtered Leads\",\n",
        "    data=csv_data,\n",
        "    file_name=\"filtered_healthcare_leads.csv\",\n",
        "    mime=\"text/csv\"\n",
        ")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vqw4sVseD5BV",
        "outputId": "6ee746b0-130d-4f36-90ef-e46c60b9171d"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Overwriting app.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "print(os.listdir())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bl3vhSdzD7DR",
        "outputId": "639be567-75ab-4cfc-fb8f-00e0b0482076"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['data', '__pycache__', 'osm_scraper.py', 'online_presence_checker.py', 'website_analyzer.py', 'scorer.py', 'contact_extractor.py', 'merge_final.py', 'app.py', 'app_backup.py', 'config_colab_backup.py', 'config.py']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 15,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cHNwTWYCAg4_",
        "outputId": "fe9d576f-730f-40f3-ef3b-f471809dadd1"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[1G\u001b[0K⠙\u001b[1G\u001b[0K⠹\u001b[1G\u001b[0K⠸\u001b[1G\u001b[0K⠼\u001b[1G\u001b[0K⠴\u001b[1G\u001b[0K⠦\u001b[1G\u001b[0K\n",
            "Collecting usage statistics. To deactivate, set browser.gatherUsageStats to false.\n",
            "\u001b[0m\n",
            "your url is: https://quiet-rivers-eat.loca.lt\n",
            "2026-06-28 16:38:08.732 Uvicorn server started on 0.0.0.0:8501\n",
            "\u001b[0m\n",
            "\u001b[34m\u001b[1m  You can now view your Streamlit app in your browser.\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m  Local URL: \u001b[0m\u001b[1mhttp://localhost:8501\u001b[0m\n",
            "\u001b[34m  Network URL: \u001b[0m\u001b[1mhttp://172.28.0.12:8501\u001b[0m\n",
            "\u001b[34m  External URL: \u001b[0m\u001b[1mhttp://35.231.153.250:8501\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m  Stopping...\u001b[0m\n",
            "^C\n"
          ]
        }
      ],
      "source": [
        "!streamlit run app.py --server.port 8501 & npx localtunnel --port 8501"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from config import FINAL_CSV\n",
        "import os\n",
        "\n",
        "print(FINAL_CSV)\n",
        "print(os.path.exists(FINAL_CSV))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "89_kYX-qGU4p",
        "outputId": "d6f9a440-945c-4d72-f0b0-a48aef6924f2"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/drive/MyDrive/healthcare_lead_gen_project/data/healthcare_leads_final.csv\n",
            "True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install streamlit pandas"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KC_s6XJEGaF7",
        "outputId": "374e7c03-7bee-43fe-a875-16458c279c67"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: streamlit in /usr/local/lib/python3.12/dist-packages (1.58.0)\n",
            "Requirement already satisfied: pandas in /usr/local/lib/python3.12/dist-packages (2.2.2)\n",
            "Requirement already satisfied: altair!=5.4.0,!=5.4.1,<7,>=4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (5.5.0)\n",
            "Requirement already satisfied: blinker<2,>=1.5.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (1.9.0)\n",
            "Requirement already satisfied: cachetools<8,>=5.5 in /usr/local/lib/python3.12/dist-packages (from streamlit) (6.2.6)\n",
            "Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (8.4.1)\n",
            "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /usr/local/lib/python3.12/dist-packages (from streamlit) (3.1.50)\n",
            "Requirement already satisfied: numpy<3,>=1.23 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.0.2)\n",
            "Requirement already satisfied: packaging>=20 in /usr/local/lib/python3.12/dist-packages (from streamlit) (26.2)\n",
            "Requirement already satisfied: pillow<13,>=7.1.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (11.3.0)\n",
            "Requirement already satisfied: pydeck<1,>=0.8.0b4 in /usr/local/lib/python3.12/dist-packages (from streamlit) (0.9.2)\n",
            "Requirement already satisfied: protobuf<8,>=3.20 in /usr/local/lib/python3.12/dist-packages (from streamlit) (5.29.6)\n",
            "Requirement already satisfied: pyarrow>=7.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (18.1.0)\n",
            "Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.32.4)\n",
            "Requirement already satisfied: tenacity<10,>=8.1.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (9.1.4)\n",
            "Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.12/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.10.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (4.15.0)\n",
            "Requirement already satisfied: starlette>=0.40.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (0.52.1)\n",
            "Requirement already satisfied: uvicorn>=0.30.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (0.49.0)\n",
            "Requirement already satisfied: httptools>=0.6.3 in /usr/local/lib/python3.12/dist-packages (from streamlit) (0.8.0)\n",
            "Requirement already satisfied: anyio>=4.0.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (4.13.0)\n",
            "Requirement already satisfied: python-multipart>=0.0.10 in /usr/local/lib/python3.12/dist-packages (from streamlit) (0.0.32)\n",
            "Requirement already satisfied: websockets>=12.0.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (15.0.1)\n",
            "Requirement already satisfied: itsdangerous>=2.1.2 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.2.0)\n",
            "Requirement already satisfied: watchdog<7,>=2.1.5 in /usr/local/lib/python3.12/dist-packages (from streamlit) (6.0.0)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.12/dist-packages (from pandas) (2.9.0.post0)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.12/dist-packages (from pandas) (2025.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.12/dist-packages (from pandas) (2026.2)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (3.1.6)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (4.26.0)\n",
            "Requirement already satisfied: narwhals>=1.14.2 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (2.22.1)\n",
            "Requirement already satisfied: idna>=2.8 in /usr/local/lib/python3.12/dist-packages (from anyio>=4.0.0->streamlit) (3.18)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.12/dist-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.12)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.12/dist-packages (from python-dateutil>=2.8.2->pandas) (1.17.0)\n",
            "Requirement already satisfied: charset_normalizer<4,>=2 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit) (3.4.7)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit) (2.5.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit) (2026.5.20)\n",
            "Requirement already satisfied: h11>=0.8 in /usr/local/lib/python3.12/dist-packages (from uvicorn>=0.30.0->streamlit) (0.16.0)\n",
            "Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.12/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.3)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.12/dist-packages (from jinja2->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (3.0.3)\n",
            "Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (26.1.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (2025.9.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (0.37.0)\n",
            "Requirement already satisfied: rpds-py>=0.25.0 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (2026.5.1)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!streamlit --version"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XY7ieyP6GdGl",
        "outputId": "d761407f-1cb7-436a-fbea-4392c58bc10c"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Streamlit, version 1.58.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!python -m py_compile app.py"
      ],
      "metadata": {
        "id": "uTRQOV1cGjJf"
      },
      "execution_count": 19,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!python -m streamlit run app.py --server.port 8501"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PO3LOVsbHBIz",
        "outputId": "990aca98-0544-4c03-9bb7-bf1848f82f6d"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Collecting usage statistics. To deactivate, set browser.gatherUsageStats to false.\n",
            "\u001b[0m\n",
            "2026-06-28 16:42:21.286 Uvicorn server started on 0.0.0.0:8501\n",
            "\u001b[0m\n",
            "\u001b[34m\u001b[1m  You can now view your Streamlit app in your browser.\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m  Local URL: \u001b[0m\u001b[1mhttp://localhost:8501\u001b[0m\n",
            "\u001b[34m  Network URL: \u001b[0m\u001b[1mhttp://172.28.0.12:8501\u001b[0m\n",
            "\u001b[34m  External URL: \u001b[0m\u001b[1mhttp://35.231.153.250:8501\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m  Stopping...\u001b[0m\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install streamlit pandas -q"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ylYwNEjoFDZd",
        "outputId": "d4fc484a-0bfb-4c74-f064-18b673246587"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Traceback (most recent call last):\n",
            "  File \"/usr/local/bin/pip3\", line 4, in <module>\n",
            "    from pip._internal.cli.main import main\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/pip/_internal/cli/main.py\", line 11, in <module>\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/pip/_internal/cli/autocompletion.py\", line 10, in <module>\n",
            "    from pip._internal.cli.main_parser import create_main_parser\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/pip/_internal/cli/main_parser.py\", line 9, in <module>\n",
            "    from pip._internal.build_env import get_runnable_pip\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/pip/_internal/build_env.py\", line 14, in <module>\n",
            "    from pip._vendor.certifi import where\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/pip/_vendor/certifi/__init__.py\", line 1, in <module>\n",
            "    from .core import contents, where\n",
            "  File \"/usr/local/lib/python3.12/dist-packages/pip/_vendor/certifi/core.py\", line 16, in <module>\n",
            "    from importlib.resources import as_file, files\n",
            "  File \"/usr/lib/python3.12/importlib/resources/__init__.py\", line 3, in <module>\n",
            "    from ._common import (\n",
            "  File \"/usr/lib/python3.12/importlib/resources/_common.py\", line 3, in <module>\n",
            "    import tempfile\n",
            "  File \"/usr/lib/python3.12/tempfile.py\", line 43, in <module>\n",
            "    import shutil as _shutil\n",
            "  File \"/usr/lib/python3.12/shutil.py\", line 30, in <module>\n",
            "    import lzma\n",
            "  File \"/usr/lib/python3.12/lzma.py\", line 27, in <module>\n",
            "    from _lzma import *\n",
            "KeyboardInterrupt\n",
            "^C\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "oGs_gEa5ExsU"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}