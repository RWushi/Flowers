PGDMP      !                |         	   turbocash    16.2    16.2     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    33132 	   turbocash    DATABASE     }   CREATE DATABASE turbocash WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Russian_Russia.1251';
    DROP DATABASE turbocash;
                postgres    false            �            1259    33138    client    TABLE     (  CREATE TABLE public.client (
    id bigint NOT NULL,
    full_name text,
    start_date date,
    end_date date,
    workplace integer,
    order_number integer DEFAULT 0,
    keys text[],
    contact text,
    days_left integer,
    term integer,
    payment integer,
    machine_guid text[]
);
    DROP TABLE public.client;
       public         heap    postgres    false            �            1259    33133    user_settings    TABLE     M   CREATE TABLE public.user_settings (
    id bigint NOT NULL,
    role text
);
 !   DROP TABLE public.user_settings;
       public         heap    postgres    false            �          0    33138    client 
   TABLE DATA           �   COPY public.client (id, full_name, start_date, end_date, workplace, order_number, keys, contact, days_left, term, payment, machine_guid) FROM stdin;
    public          postgres    false    216   �       �          0    33133    user_settings 
   TABLE DATA           1   COPY public.user_settings (id, role) FROM stdin;
    public          postgres    false    215   �       !           2606    33146    client client_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.client
    ADD CONSTRAINT client_pkey PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.client DROP CONSTRAINT client_pkey;
       public            postgres    false    216                       2606    33142     user_settings user_settings_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public.user_settings
    ADD CONSTRAINT user_settings_pkey PRIMARY KEY (id);
 J   ALTER TABLE ONLY public.user_settings DROP CONSTRAINT user_settings_pkey;
       public            postgres    false    215            "           2606    33147    client fk_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.client
    ADD CONSTRAINT fk_id FOREIGN KEY (id) REFERENCES public.user_settings(id) ON DELETE CASCADE NOT VALID;
 6   ALTER TABLE ONLY public.client DROP CONSTRAINT fk_id;
       public          postgres    false    216    4639    215            �     x����n�@���)� �`�����p��m��	�����|�*E��v�e��� �R�JH��
�7�A��T:#�3g���`Z�,GS�+ّ-���#O�'�E6g���=��|iK~��/�[����d���n��_�1
��E1<�N2���j�/_�J�sgZ2憛~���`� ��f�)#�?6�:���ri�'�E�1��E>�eor��ow���d���ʯg�恡�����b���@i#�yB+�a����p���&Թ��� ��2����݉w��P�;ZT+
$�3��Z�ҕ�b,W�\l*�#&��w���e +��xP�4A�^���=�g�� ���,#�i��D�|ܿg��|��"�}=H�%K��CT��-�p�z!H����_Usl�F�.�j�>��a�/���MU���0(+��\c�u!U/���ؖ/�����:���ʩB�8B�:��;@�����X�R���"(���瀢i2^��W��&׆�K�����iQ��9_���g(ܞ
�?���}      �   W   x�5ȹ�0 �:ى�]h���ٟ��)U%Ҽ��/�T0�Y���EY�C6!ϑ�{�Ǵl��X	̤��d�n��_� <{7�     