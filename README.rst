==============================
Simple URL fetching for Zegami
==============================

Script to fetch images given in a tsv file column for use with Zegami.


Usage
-----

Download images from 'fullimgurl' column in INPUT_URL to this directory:

.. code::

    $ ./datadownload.py -i INPUT_URL

Download image and write back out tsv to OUTPUT_FILE:

.. code::

    $ ./datadownload.py -i INPUT_URL -o OUTPUT_FILE


Download using COLUMN and write images to OUTPUT_DIR:

.. code::

    $ ./datadownload.py -i INPUT_URL -c COLUMN -d OUTPUT_DIR
