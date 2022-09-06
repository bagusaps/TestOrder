# Create Order

## Bagaimana cara kerjanya?
Di dalam directory test terdapat test_order.py. di dalamnya terdapat test_create_order. function/testcase tersebut akan menjalankan API yg terdapat dalam api_client.order untuk membuat order. ketika API telah di hit nantinya terdapat response dan kita akan cek di dalam response tersebut untuk order_status dengan value "NEW" dan last_updated_timestamp tidak empty

## Apa saja yang perlu di install?
disni saya menggunakan pytest dan di dalamnya saya install request dan assertpy