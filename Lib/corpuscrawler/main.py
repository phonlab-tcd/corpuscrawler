# Copyright 2017 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import, print_function, unicode_literals
import argparse
import sys
from corpuscrawler import (
    crawl_am, crawl_be, crawl_bg, crawl_bm, crawl_bn, crawl_bs,
    crawl_ccp, crawl_el, crawl_fa, crawl_fo, crawl_fuv,
    crawl_gsw, crawl_gv, crawl_ha, crawl_hi, crawl_hr,
    crawl_id, crawl_ig, crawl_kj, crawl_kk, crawl_ky, crawl_lo, crawl_mnw,
    crawl_mk, crawl_mt, crawl_my, crawl_pl, crawl_ps,
    crawl_rm, crawl_ro, crawl_ru, crawl_rw, crawl_shn,
    crawl_sr, crawl_so, crawl_sq, crawl_sw, crawl_ta,
    crawl_taq, crawl_tr, crawl_ug, crawl_uk, crawl_ur, crawl_yo,
)
from corpuscrawler.util import Crawler


def main():
    crawls = {
        'am': crawl_am.crawl,    # Amharic
        'be': crawl_be.crawl,    # Belarusian
        'bg': crawl_bg.crawl,    # Bulgarian
        'bm': crawl_bm.crawl,    # Bambara
        'bn': crawl_bn.crawl,    # Bangla
        'bs': crawl_bs.crawl,    # Bosnian
        'ccp': crawl_ccp.crawl,  # Chakma
        'el': crawl_el.crawl,    # Greek
        'fa': crawl_fa.crawl,    # Persian
        'fo': crawl_fo.crawl,    # Faroese
        'fuv': crawl_fuv.crawl,  # Nigerian Fulfulde
        'gsw': crawl_gsw.crawl,  # Swiss German
        'gv': crawl_gv.crawl,    # Manx Gaelic
        'ha': crawl_ha.crawl,    # Hausa
        'hi': crawl_hi.crawl,    # Hindi
        'hr': crawl_hr.crawl,    # Croatian
        'id': crawl_id.crawl,    # Indonesian
        'ig': crawl_ig.crawl,    # Igbo
        'kj': crawl_kj.crawl,    # Kuanyama
        'kk': crawl_kk.crawl,    # Kazakh
        'ky': crawl_ky.crawl,    # Kyrgyz
        'lo': crawl_lo.crawl,    # Lao
        'mk': crawl_mk.crawl,    # Macedonian
        'mnw': crawl_mnw.crawl,  # Mon
        'mt': crawl_mt.crawl,    # Maltese
        'my': crawl_my.crawl,    # Burmese
        'pl': crawl_pl.crawl,    # Polish
        'ps': crawl_ps.crawl,    # Pashto
        'rm': crawl_rm.crawl,    # Romansh
        'ro': crawl_ro.crawl,    # Romanian
        'ru': crawl_ru.crawl,    # Russian
        'rw': crawl_rw.crawl,    # Kinyarwanda
        'shn': crawl_shn.crawl,  # Shan
        'so': crawl_so.crawl,    # Somali
        'sq': crawl_sq.crawl,    # Albanian
        'sr': crawl_sr.crawl,    # Serbian
        'sw': crawl_sw.crawl,    # Swahili
        'ta': crawl_ta.crawl,    # Tamil
        'taq': crawl_taq.crawl,  # Tamasheq
        'tr': crawl_tr.crawl,    # Turkish
        'ug': crawl_ug.crawl,    # Uyghur
        'uk': crawl_uk.crawl,    # Ukrainian
        'ur': crawl_ur.crawl,    # Urdu
        'yo': crawl_yo.crawl,    # Yoruba
    }
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--language', default='rm', choices=sorted(crawls.keys()),
        help='IETF BCP47 language code for the corpus to be crawled')
    parser.add_argument(
        '--output', default='./corpus',
        help='path to directory for writing output')
    parser.add_argument(
        '--cache', default='./cache-corpuscrawler',
        help='path to directory for caching fetched files')
    args = parser.parse_args()

    crawler = Crawler(language=args.language, output_dir=args.output,
                      cache_dir=args.cache)
    crawls[args.language](crawler)
    crawler.close()
