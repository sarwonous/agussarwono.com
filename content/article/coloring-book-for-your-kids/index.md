---
title: "Coloring Book for Your Kids"
date: 2024-11-28T16:12:52+07:00
draft: true
---

Hi para bapak bapak, untuk artikel kali ini kita akan membahas sedikit tentang bonding dengan anak. di sini kita akan sedikit memberi contoh salah satu kegiatan yang bisa kita lakukan unutk bisa lebih dekat ke anak, contohnya adalah dengan kegiatan mewarnai

Mewarnai

Aktifitas mewarnai pada anak dapat membantu merangsang imajinasi anak, terutama untuk mewarnai gambar2 non fiksi yang mengharuskan anak untuk menggunakan imajinasinya, selain kreatifitas anak, mewarnai dapat juga dilakukan untuk meningkatkan konsentrasi anak, anak diajarkan untuk bisa berkonsentrasi saat mewarnai dengan mengikuti pola dengan baik.

Persiapan

Bahan
 - Buku Mewarnai
 - Alat Mewarnai Spidol, Pensil Warna, Crayon.

untuk memudahkan para bapak, berikut ini kami sertakan link untuk mngunduh buku mewarnai yang telah berhasil kami himpun

<LINK>

nb:

untuk bapak2 heker berikut saya sertakan juga script untuk download buku mewarnai tersebut


```js
const https = require('https');
const fs = require('fs');

const regex = /figure\sclass\=\"([a-zA-Z0-9-\s]+?)\"\>\<a href="(.*?\.pdf)"/gm;

// return a html string
function fetch(url) {
    return new Promise((resolve, reject) => {
        https.get(url, {
            headers: {
                'User-Agent': 'Mozilla/5.0'
            }
        }, (res) => {
            let data = '';
            res.on('data', (chunk) => {
                data += chunk;
            });
            res.on('end', () => {
                resolve(data);
            });
        }).on('error', (error) => {
            reject(error);
        });
    });
}

function download(url) {
    
    let m;
    let cleanURL = url;
    if (cleanURL.charAt(url.length - 1) === '/') {
        cleanURL = url.slice(0, -1);
    }
    let folder = cleanURL.split('/').pop();
    if (!fs.existsSync(`./pdfs/${folder}`)) {
        fs.mkdirSync(`./pdfs/${folder}`);
    }
    fetch(url).then((data) => {
        const str = data;
        while ((m = regex.exec(str)) !== null) {
            if (m.index === regex.lastIndex) {
                regex.lastIndex++;
            }
            // goupe 2 is the pdf link
            console.log(m[2]);
            console.log('----------------------');
            const url = m[2];
            // download and save the pdf
            https.get(url, {
                headers: {
                    'User-Agent': 'Mozilla/5.0'
                }
            }, (res) => {
                const path = `./pdfs/${folder}/${url.split('/').pop()}`;
                const file = fs.createWriteStream(path);
                res.pipe(file);
                file.on('finish', () => {
                    file.close();
                    console.log(`Downloaded ${url}`);
                });
            });
        }
    }).catch((error) => {
        console.error(`Failed to fetch ${url}: ${error.message}`);
    });
};

if (!fs.existsSync('./pdfs')) {
    fs.mkdirSync('./pdfs');
}

const url = process.argv[2];
if (!url) {
    console.error('Please provide a URL');
    process.exit(1);
}
if (url.indexOf('http') !== 0) {
    console.error('Invalid URL');
    process.exit(1);
}
if (url.indexOf('mondaymandala') === -1) {
    console.error('Invalid URL, only mondaymandala.com is supported');
    process.exit(1);
}
download(url);
```


```shell
