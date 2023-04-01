import streamlit as st
import os
import json
import pandas as pd
import sqlite3
import plotly_express as px


st.title('PhonePe Pulse Data Visualization 2018 to 2022')


# CREATING CONNECTION WITH SQL SERVER
connection = sqlite3.connect("phonepe.db")
cursor = connection.cursor()

# Creating Options in app


with st.container():
        st.title("Basic Search")
        #st.write("----")
        
        options = ["select","Top 10 states based on year and amount of transaction","Least 10 states based on type and amount of transaction",
                "Top 10 mobile brands based on percentage of transaction","Top 10 Registered-users based on States and District(pincode)",
                "Top 10 Districts based on states and amount of transaction","Least 10 Districts based on states and amount of transaction",
                "Least 10 registered-users based on Districts and states","Top 10 transactions_type based on states and transaction_amount",
                "Perhead to calculate no of Trancations in districts"]
        select = st.selectbox("Select the option",options)
        if select=="select":
            cursor.execute("SELECT Year,SUM(Transacion_amount) AS Total_amount FROM aggregated_Transaction GROUP BY Year");
            df = pd.DataFrame(cursor.fetchall(),columns=['Year','Transaction_amount'])
            col1,col2 = st.columns(2)
            with col1:
                st.write(df)
            with col2:
                st.title("Top 10 states based on type and amount of transaction")
                fig=px.bar(df,x="Year",y="Transaction_amount")
                tab1, tab2 = st.tabs(["Streamlit theme (default)",'simple_white'])
                with tab1:
                    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
                with tab2:
                    st.plotly_chart(fig, theme=None, use_container_width=True)
        elif select=="Top 10 states based on year and amount of transaction":
            cursor.execute("SELECT DISTINCT State,Transaction_amount,Year,Quater FROM top_transaction GROUP BY State ORDER BY Transaction_amount DESC LIMIT 10");
            df = pd.DataFrame(cursor.fetchall(),columns=['State','Transaction_amount','Year','Quater'])
            col1,col2 = st.columns(2)
            with col1:
                st.write(df)
            with col2:
                st.title("Top 10 states based on type and amount of transaction")
                fig=px.bar(df,x="State",y="Transaction_amount")
                tab1, tab2 = st.tabs(["Streamlit theme (default)", "simple_white"])
                with tab1:
                    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
                with tab2:
                    st.plotly_chart(fig, theme=None, use_container_width=True)

        elif select=="Least 10 states based on type and amount of transaction":
            cursor.execute("SELECT DISTINCT State,Transaction_amount,Year,Quater FROM top_transaction GROUP BY State ORDER BY Transaction_amount ASC LIMIT 10");
            df = pd.DataFrame(cursor.fetchall(),columns=['State','Transaction_amount','Year','Quater'])
            col1,col2 = st.columns(2)
            with col1:
                st.write(df)
            with col2:
                st.title("Least 10 states based on type and amount of transaction")
                fig=px.bar(df,x="State",y="Transaction_amount")
                tab1, tab2 = st.tabs(["Streamlit theme (default)", "simple_white"])
                with tab1:
                    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
                with tab2:
                    st.plotly_chart(fig, theme=None, use_container_width=True)

        elif select=="Top 10 mobile brands based on percentage of transaction":
            cursor.execute("SELECT DISTINCT phone_brand,phone_percentage FROM aggregated_user GROUP BY phone_brand ORDER BY phone_percentage DESC LIMIT 10");
            df = pd.DataFrame(cursor.fetchall(),columns=['phone_brands','phone_percentage'])
            col1,col2 = st.columns(2)
            with col1:
                st.write(df)
            with col2:
                st.title("Top 10 mobile brands based on percentage of transaction")
                fig=px.bar(df,x="phone_brands",y="phone_percentage")
                tab1, tab2 = st.tabs(["Streamlit theme (default)", "simple_white"])
                with tab1:
                    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
                with tab2:
                    st.plotly_chart(fig, theme=None, use_container_width=True)

        elif select=="Top 10 Registered-users based on States and District(pincode)":
            cursor.execute("SELECT DISTINCT State,district_name,registered_users FROM top_user GROUP BY State ORDER BY registered_users DESC LIMIT 10");
            df = pd.DataFrame(cursor.fetchall(),columns=['State','district_name','registered_users'])
            col1,col2 = st.columns(2)
            with col1:
                st.write(df)
            with col2:
                st.title("Top 10 Registered-users based on States and District(pincode)")
                fig=px.bar(df,x="State",y="registered_users")
                tab1, tab2 = st.tabs(["Streamlit theme (default)", "simple_white"])
                with tab1:
                    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
                with tab2:
                    st.plotly_chart(fig, theme=None, use_container_width=True)

        elif select=="Top 10 Districts based on states and amount of transaction":
            cursor.execute("SELECT DISTINCT State,district,Transaction_amount FROM map_transaction GROUP BY State ORDER BY Transaction_amount DESC LIMIT 10");
            df = pd.DataFrame(cursor.fetchall(),columns=['State','district','Transaction_amount'])
            col1,col2 = st.columns(2)
            with col1:
                st.write(df)
            with col2:
                st.title("Top 10 Districts based on states and amount of transaction")
                fig=px.bar(df,x="State",y="Transaction_amount")
                tab1, tab2 = st.tabs(["Streamlit theme (default)", "simple_white"])
                with tab1:
                    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
                with tab2:
                    st.plotly_chart(fig, theme=None, use_container_width=True)

        elif select=="Least 10 Districts based on states and amount of transaction":
            cursor.execute("SELECT DISTINCT State,district,Transaction_amount FROM map_transaction GROUP BY State ORDER BY Transaction_amount ASC LIMIT 10");
            df = pd.DataFrame(cursor.fetchall(),columns=['State','district','Transaction_amount'])
            col1,col2 = st.columns(2)
            with col1:
                st.write(df)
            with col2:
                st.title("Least 10 Districts based on states and amount of transaction")
                fig=px.bar(df,x="State",y="Transaction_amount")
                tab1, tab2 = st.tabs(["Streamlit theme (default)", "simple_white"])
                with tab1:
                    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
                with tab2:
                    st.plotly_chart(fig, theme=None, use_container_width=True)

        elif select=="Least 10 registered-users based on Districts and states":
            cursor.execute("SELECT DISTINCT State,district_name,registered_users FROM top_user GROUP BY State ORDER BY registered_users ASC LIMIT 10");
            df = pd.DataFrame(cursor.fetchall(),columns=['State','district_name','registered_users'])
            col1,col2 = st.columns(2)
            with col1:
                st.write(df)
            with col2:
                st.title("Least 10 registered-users based on Districts and states")
                fig=px.bar(df,x="State",y="registered_users")
                tab1, tab2 = st.tabs(["Streamlit theme (default)", "simple_white"])
                with tab1:
                    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
                with tab2:
                    st.plotly_chart(fig, theme=None, use_container_width=True)

        elif select=="Top 10 transactions_type based on states and transaction_amount":
            cursor.execute("SELECT DISTINCT State,Transacion_type,Transacion_amount FROM aggregated_transaction GROUP BY State,Transacion_type ORDER BY Transacion_amount DESC LIMIT 10");
            df = pd.DataFrame(cursor.fetchall(),columns=['State','Transacion_type','Transacion_amount'])
            col1,col2 = st.columns(2)
            with col1:
                st.write(df)
            with col2:
                st.title("Top 10 transactions_type based on states and transaction_amount")
                fig=px.bar(df,x="State",y="Transacion_amount")
                tab1, tab2 = st.tabs(["Streamlit theme (default)", "simple_white"])
                with tab1:
                    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
                with tab2:
                    st.plotly_chart(fig, theme=None, use_container_width=True)
        elif select=="Perhead to calculate no of Trancations in districts":
            cursor.execute("SELECT DISTINCT State,(Transaction_amount/Transaction_count) AS percentage FROM top_transaction GROUP BY State ORDER BY (Transaction_amount/Transaction_count) ASC LIMIT 10");
            df = pd.DataFrame(cursor.fetchall(),columns=['State','Transaction_amount',])
            col1,col2 = st.columns(2)
            with col1:
                st.write(df)
            with col2:
                st.title("Perhead to calculate no of Trancations in districts")
                fig=px.bar(df,x="State",y="Transaction_amount")
                tab1, tab2 = st.tabs(["Streamlit theme (default)", "simple_white"])
                with tab1:
                    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
                with tab2:
                    st.plotly_chart(fig, theme=None, use_container_width=True)
   



with st.container():
        st.title("select category")
        Topic = ["","brand","district","registered-users","Top-Transactions","Transaction-Type"]
        choice_topic = st.selectbox("Search by",Topic)

    #creating functions for query search in sqlite to get the data
        def type_(type):
            cursor.execute(f"SELECT DISTINCT State,Quater,Year,Transacion_type,Transacion_amount FROM aggregated_transaction WHERE Transacion_type = '{type}' ORDER BY State,Quater,Year");
            df = pd.DataFrame(cursor.fetchall(), columns=['State','Quater', 'Year', 'Transacion_type', 'Transacion_amount'])
            return df
        def type_year(year,type):
            cursor.execute(f"SELECT DISTINCT State,Year,Quater,Transacion_type,Transacion_amount FROM aggregated_transaction WHERE Year = '{year}' AND Transacion_type = '{type}' ORDER BY State,Quater,Year");
            df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'Transacion_type', 'Transacion_amount'])
            return df
        def type_state(state,year,type):
            cursor.execute(f"SELECT DISTINCT State,Year,Quater,Transacion_type,Transacion_amount FROM aggregated_transaction WHERE State = '{state}' AND Transacion_type = '{type}' And Year = '{year}' ORDER BY State,Quater,Year");
            df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'Transacion_type', 'Transacion_amount'])
            return df
        def district_choice_state(_state):
            cursor.execute(f"SELECT DISTINCT State,Year,Quater,district,Transaction_amount FROM map_transaction WHERE State = '{_state}' ORDER BY State,Year,Quater,district");
            df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'district', 'Transaction_amount'])
            return df
        def dist_year_state(year,_state):
            cursor.execute(f"SELECT DISTINCT State,Year,Quater,district,Transaction_amount FROM map_transaction WHERE Year = '{year}' AND State = '{_state}' ORDER BY State,Year,Quater,district");
            df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'district', 'Transaction_amount'])
            return df
        def district_year_state(_dist,year,_state):
            cursor.execute(f"SELECT DISTINCT State,Year,Quater,district,Transaction_amount FROM map_transaction WHERE district = '{_dist}' AND State = '{_state}' AND Year = '{year}' ORDER BY State,Year,Quater,district");
            df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'district', 'Transaction_amount'])
            return df
        def brand_(brand_type):
            cursor.execute(f"SELECT State,Year,Quater,phone_brand,phone_percentage FROM aggregated_user WHERE phone_brand='{brand_type}' ORDER BY State,Year,Quater,phone_brand,phone_percentage DESC");
            df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'phone_brand', 'phone_percentage'])
            return df
        def brand_year(brand_type,year):
            cursor.execute(f"SELECT State,Year,Quater,phone_brand,phone_percentage FROM aggregated_user WHERE Year = '{year}' AND phone_brand='{brand_type}' ORDER BY State,Year,Quater,phone_brand,phone_percentage DESC");
            df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'phone_brand', 'phone_percentage'])
            return df
        def brand_state(state,brand_type,year):
            cursor.execute(f"SELECT State,Year,Quater,phone_brand,phone_percentage FROM aggregated_user WHERE State = '{state}' AND phone_brand='{brand_type}' AND Year = '{year}' ORDER BY State,Year,Quater,phone_brand,phone_percentage DESC");
            df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'phone_brand', 'phone_percentage'])
            return df
        def transaction_state(_state):
            cursor.execute(f"SELECT State,Year,Quater,Transaction_districts,Transaction_count,Transaction_amount FROM top_transaction WHERE State = '{_state}' GROUP BY State,Year,Quater")
            df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'Transaction_districts', 'Transaction_count', 'Transaction_amount'])
            return df
        def transaction_year(_state,_year):
            cursor.execute(f"SELECT State,Year,Quater,Transaction_districts,Transaction_count,Transaction_amount FROM top_transaction WHERE Year = '{_year}' AND State = '{_state}' GROUP BY State,Year,Quater")
            df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'Transaction_districts', 'Transaction_count', 'Transaction_amount'])
            return df
        def transaction_quater(_state,_year,_quater):
            cursor.execute(f"SELECT State,Year,Quater,Transaction_districts,Transaction_count,Transaction_amount FROM top_transaction WHERE Year = '{_year}' AND Quater = '{_quater}' AND State = '{_state}' GROUP BY State,Year,Quater")
            df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'Transaction_districts', 'Transaction_count', 'Transaction_amount'])
            return df
        def registered_user_state(_state):
            cursor.execute(f"SELECT State,Year,Quater,district,map_registered_users FROM map_user WHERE State = '{_state}' ORDER BY State,Year,Quater,district")
            df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'district', 'map_registered_users'])
            return df
        def registered_user_year(_state,_year):
            cursor.execute(f"SELECT State,Year,Quater,district,map_registered_users FROM map_user WHERE Year = '{_year}' AND State = '{_state}' ORDER BY State,Year,Quater,district")
            df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'district', 'map_registered_users'])
            return df
        def registered_user_district(_state,_year,_dist):
            cursor.execute(f"SELECT State,Year,Quater,district,map_registered_users FROM map_user WHERE Year = '{_year}' AND State = '{_state}' AND district = '{_dist}' ORDER BY State,Year,Quater,district")
            df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'district', 'map_registered_users'])
            return df


        if choice_topic=="Transaction-Type":
            col1,col2,col3 = st.columns(3)
            with col1:
                st.subheader(" TRANSACTION TYPE ")
                transaction_type = st.selectbox("search by", ["Choose an option", "Financial Services",
                                                            "Merchant payments", "Peer-to-peer payments",
                                                            "Recharge & bill payments", "Others"], 0)
            with col2:
                st.subheader(" SELECT THE YEAR ")
                choice_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
            with col3:
                st.subheader(" SELECT STATE ")
                menu_state = ['', 'andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
                            'assam', 'bihar', 'chandigarh', 'chhattisgarh', 'dadra-&-nagar-haveli-&-daman-&-diu',
                            'delhi', 'goa', 'gujarat', 'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
                            'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh', 'maharashtra', 'manipur',
                            'meghalaya', 'mizoram', 'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
                            'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh', 'uttarakhand', 'west-bengal']
                choice_state = st.selectbox("State", menu_state, 0)

            if transaction_type:
                col1,col2,col3, = st.columns(3)
                with col1:
                    st.subheader(f'{transaction_type}')
                    st.write(type_(transaction_type))
            if transaction_type and choice_year:
                with col2:
                    st.subheader(f' in {choice_year}')
                    st.write(type_year(choice_year,transaction_type))
            if transaction_type and choice_state and choice_year:
                with col3:
                    st.subheader(f' in {choice_state}')
                    st.write(type_state(choice_state,choice_year,transaction_type))

        if choice_topic=="district":
            col1,col2,col3 = st.columns(3)
            with col1:
                st.subheader(" SELECT STATE ")
                menu_state = ['', 'andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
                            'assam', 'bihar', 'chandigarh', 'chhattisgarh', 'dadra-&-nagar-haveli-&-daman-&-diu',
                            'delhi', 'goa', 'gujarat', 'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
                            'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh', 'maharashtra', 'manipur',
                            'meghalaya', 'mizoram', 'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
                            'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh', 'uttarakhand', 'west-bengal']
                choice_state = st.selectbox("State", menu_state, 0)
            with col2:
                st.subheader(" SELECT YEAR ")
                choice_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
            with col3:
                st.subheader(" SELECT DISTRICT ")
               
                df = pd.read_sql_query('SELECT DISTINCT district,State FROM map_transaction GROUP BY  district',connection)
                list = df['district'].tolist()

                menu_dist = ['',*list]
                district = st.selectbox("district", menu_dist, 0)
            if choice_state:
                col1,col2,col3 = st.columns(3)
                with col1:
                    st.subheader(f'{choice_state}')
                    st.write(district_choice_state(choice_state))
            if choice_year and choice_state:
                with col2:
                    st.subheader(f'in {choice_year} ')
                    st.write(dist_year_state(choice_year,choice_state))
            if district and choice_state and choice_year:
                with col3:
                    st.subheader(f'in {district} ')
                    st.write(district_year_state(district,choice_year,choice_state))

        if choice_topic=="brand":
            col1,col2,col3 = st.columns(3)
            with col1:
                st.subheader(" SELECT BRAND ")
                mobiles = ['', 'Apple', 'Asus', 'COOLPAD', 'Gionee', 'HMD Global', 'Huawei',
                        'Infinix', 'Lava', 'Lenovo', 'Lyf', 'Micromax', 'Motorola', 'OnePlus',
                        'Oppo','Realme', 'Samsung', 'Tecno', 'Vivo', 'Xiaomi','Others']
                brand_type = st.selectbox("search by",mobiles, 0)
            with col2:
                st.subheader(" SELECT YEAR ")
                choice_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
            with col3:
                st.subheader(" SELECT STATE ")
                menu_state = ['', 'andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
                            'assam', 'bihar', 'chandigarh', 'chhattisgarh', 'dadra-&-nagar-haveli-&-daman-&-diu',
                            'delhi', 'goa', 'gujarat', 'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
                            'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh', 'maharashtra', 'manipur',
                            'meghalaya', 'mizoram', 'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
                            'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh', 'uttarakhand', 'west-bengal']
                choice_state = st.selectbox("State", menu_state, 0)

            if brand_type:
                col1,col2,col3, = st.columns(3)
                with col1:
                    st.subheader(f'{brand_type}')
                    st.write(brand_(brand_type))
            if brand_type and choice_year:
                with col2:
                    st.subheader(f' in {choice_year}')
                    st.write(brand_year(brand_type,choice_year))
            if brand_type and choice_state and choice_year:
                with col3:
                    st.subheader(f' in {choice_state}')
                    st.write(brand_state(choice_state,brand_type,choice_year))

        if choice_topic=="Top-Transactions":
            col1,col2,col3 = st.columns(3)
            with col1:
                st.subheader(" SELECT STATE ")
                menu_state = ['', 'andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
                            'assam', 'bihar', 'chandigarh', 'chhattisgarh', 'dadra-&-nagar-haveli-&-daman-&-diu',
                            'delhi', 'goa', 'gujarat', 'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
                            'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh', 'maharashtra', 'manipur',
                            'meghalaya', 'mizoram', 'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
                            'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh', 'uttarakhand', 'west-bengal']
                choice_state = st.selectbox("State", menu_state, 0)
            with col2:
                st.subheader(" SELECT YEAR ")
                choice_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
            with col3:
                st.subheader(" SELECT Quater ")
                menu_quater = ["", "1", "2", "3", "4"]
                choice_quater = st.selectbox("Quater", menu_quater, 0)

            if choice_state:
                with col1:
                    st.subheader(f'{choice_state}')
                    st.write(transaction_state(choice_state))
            if choice_state and choice_year:
                with col2:
                    st.subheader(f'{choice_year}')
                    st.write(transaction_year(choice_state,choice_year))
            if choice_state and choice_quater:
                with col3:
                    st.subheader(f'{choice_quater}')
                    st.write(transaction_quater(choice_state,choice_year,choice_quater))

        if choice_topic=="registered-users":
            col1,col2,col3 = st.columns(3)
            with col1:
                st.subheader(" SELECT STATE ")
                menu_state = ['', 'andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
                            'assam', 'bihar', 'chandigarh', 'chhattisgarh', 'dadra-&-nagar-haveli-&-daman-&-diu',
                            'delhi', 'goa', 'gujarat', 'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
                            'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh', 'maharashtra', 'manipur',
                            'meghalaya', 'mizoram', 'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
                            'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh', 'uttarakhand', 'west-bengal']
                choice_state = st.selectbox("State", menu_state, 0)
            with col2:
                st.subheader(" SELECT YEAR ")
                choice_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
            with col3:
                st.subheader(" SELECT DISTRICT ")
                df = pd.read_sql_query('SELECT DISTINCT district FROM map_transaction GROUP BY State,district',connection)
                list = df["district"].unique().tolist()
                menu_dist = ['',*list]
                district = st.selectbox("district", menu_dist, 0)

            if choice_state:
                with col1:
                    st.subheader(f'{choice_state}')
                    st.write(registered_user_state(choice_state))
            if choice_state and choice_year:
                with col2:
                    st.subheader(f'{choice_year}')
                    st.write(registered_user_year(choice_state,choice_year))
            if choice_state and choice_year and district:
                with col3:
                    st.subheader(f'{district}')
                    st.write(registered_user_district(choice_state,choice_year,district))
