#!/usr/bin/env python3

import pandas as pd

config = "231013_borrowing_mapping.ods" # use argument
df = pd.read_excel(config, index_col=None)

# print(df)
domain = "https://git-codecommit.eu-central-1.amazonaws.com/v1/repos/"
# template = ff"pisa_2025ft_translation_{locale}_{step}.git"

repos = ["pisa_2025ft_translation_LOCALE_adaptation", "pisa_2025ft_translation_LOCALE_prepare-files", "pisa_2025ft_translation_LOCALE_translation1", "pisa_2025ft_translation_LOCALE_translation2", "pisa_2025ft_translation_LOCALE_reconciliation", "pisa_2025ft_translation_LOCALE_verification-preparation", "pisa_2025ft_translation_LOCALE_verification", "pisa_2025ft_translation_LOCALE_verification-review", "pisa_2025ft_translation_LOCALE_post-verification-review", "pisa_2025ft_translation_LOCALE_final-check-preparation", "pisa_2025ft_translation_LOCALE_final-check", "pisa_2025ft_translation_LOCALE_final-check-review"]

locales = ["ar-AE", "ar-IL", "ar-JO", "ar-MA", "ar-PS", "ar-QA", "ar-SA", "az-GE", "az-QZ", "bg-BG", "ca-ES", "ca-ES-valencia", "cnr-ME", "cs-CZ", "da-DK", "de-AT", "de-BE", "de-CH", "de-DE", "de-IT", "de-LU", "el-CY", "el-GR", "en-AE", "en-AU", "en-BN", "en-CA", "en-CY", "en-GB-scotland", "en-GB-x-excscotl", "en-HK", "en-IE", "en-KE", "en-LB", "en-LU", "en-MO", "en-MT", "en-MU", "en-MY", "en-NZ", "en-PH", "en-PS", "en-QA", "en-SA", "en-SE", "en-SG", "en-US", "en-ZM", "es-AR", "es-CL", "es-CO", "es-CR", "es-DO", "es-EC", "es-ES", "es-GT", "es-MX", "es-PA", "es-PE", "es-PY", "es-UY", "et-EE", "eu-ES", "fi-FI", "fo-DK", "fr-BE", "fr-CA", "fr-CH", "fr-FR", "fr-LB", "fr-LU", "fr-MA", "ga-IE", "gl-ES", "he-IL", "hr-HR", "hu-HU", "hu-RO", "hu-RS", "hu-SK", "hy-AM", "id-ID", "is-IS", "it-CH", "it-IT", "it-ZZ", "ja-JP", "ka-GE", "kaa-UZ", "kk-KZ", "kk-MN", "ko-KR", "ku-IQ", "ky-KG", "lt-LT", "lv-LV", "mn-MN", "ms-BN", "ms-MY", "mt-MT", "nb-NO", "nl-BE", "nl-NL", "nn-NO", "pl-LT", "pl-PL", "pt-BR", "pt-MO", "pt-PT", "ro-MD", "ro-RO", "ru-EE", "ru-GE", "ru-KG", "ru-KZ", "ru-LT", "ru-LV", "ru-MD", "ru-QZ", "ru-UZ", "sk-SK", "sl-SI", "sq-AL", "sq-ME", "sq-XK", "sr-RS", "sr-XK", "sv-FI", "sv-SE", "tg-TJ", "th-TH", "tr-TR", "uk-UA", "uz-KG", "uz-UZ", "zh-HK", "zh-MO", "zh-TW"]

locale = "gl-ES"
for step in repos:
    print(step.replace("LOCALE", locale))
    url = f"{domain}{step}.git"
    print(url)
    # try:


# "pisa_2025ft_translation_LOCALE_adaptation", "pisa_2025ft_translation_LOCALE_prepare-files", "pisa_2025ft_translation_LOCALE_translation1", "pisa_2025ft_translation_LOCALE_translation2", "pisa_2025ft_translation_LOCALE_reconciliation", "pisa_2025ft_translation_LOCALE_verification-preparation", "pisa_2025ft_translation_LOCALE_verification", "pisa_2025ft_translation_LOCALE_verification-review", "pisa_2025ft_translation_LOCALE_post-verification-review", "pisa_2025ft_translation_LOCALE_final-check-preparation", "pisa_2025ft_translation_LOCALE_final-check", "pisa_2025ft_translation_LOCALE_final-check-review"]

# locales = ["ar-AE", "ar-IL", "ar-JO", "ar-MA", "ar-PS", "ar-QA", "ar-SA", "az-GE", "az-QZ", "bg-BG", "ca-ES", "ca-ES-valencia", "cnr-ME", "cs-CZ", "da-DK", "de-AT", "de-BE", "de-CH", "de-DE", "de-IT", "de-LU", "el-CY", "el-GR", "en-AE", "en-AU", "en-BN", "en-CA", "en-CY", "en-GB-scotland", "en-GB-x-excscotl", "en-HK", "en-IE", "en-KE", "en-LB", "en-LU", "en-MO", "en-MT", "en-MU", "en-MY", "en-NZ", "en-PH", "en-PS", "en-QA", "en-SA", "en-SE", "en-SG", "en-US", "en-ZM", "es-AR", "es-CL", "es-CO", "es-CR", "es-DO", "es-EC", "es-ES", "es-GT", "es-MX", "es-PA", "es-PE", "es-PY", "es-UY", "et-EE", "eu-ES", "fi-FI", "fo-DK", "fr-BE", "fr-CA", "fr-CH", "fr-FR", "fr-LB", "fr-LU", "fr-MA", "ga-IE", "gl-ES", "he-IL", "hr-HR", "hu-HU", "hu-RO", "hu-RS", "hu-SK", "hy-AM", "id-ID", "is-IS", "it-CH", "it-IT", "it-ZZ", "ja-JP", "ka-GE", "kaa-UZ", "kk-KZ", "kk-MN", "ko-KR", "ku-IQ", "ky-KG", "lt-LT", "lv-LV", "mn-MN", "ms-BN", "ms-MY", "mt-MT", "nb-NO", "nl-BE", "nl-NL", "nn-NO", "pl-LT", "pl-PL", "pt-BR", "pt-MO", "pt-PT", "ro-MD", "ro-RO", "ru-EE", "ru-GE", "ru-KG", "ru-KZ", "ru-LT", "ru-LV", "ru-MD", "ru-QZ", "ru-UZ", "sk-SK", "sl-SI", "sq-AL", "sq-ME", "sq-XK", "sr-RS", "sr-XK", "sv-FI", "sv-SE", "tg-TJ", "th-TH", "tr-TR", "uk-UA", "uz-KG", "uz-UZ", "zh-HK", "zh-MO", "zh-TW"]