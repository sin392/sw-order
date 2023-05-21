SET @common_id_00 := "00000000-0000-0000-0000-000000000000",
    @common_id_01 := "11111111-1111-1111-1111-111111111111",
    @common_id_02 := "22222222-2222-2222-2222-222222222222",
    @common_id_03 := "33333333-3333-3333-3333-333333333333",
    @common_id_04 := "44444444-4444-4444-4444-444444444444",
    @common_id_05 := "55555555-5555-5555-5555-555555555555",
    @common_id_06 := "66666666-6666-6666-6666-666666666666",
    @common_id_07 := "77777777-7777-7777-7777-777777777777",
    @common_id_08 := "88888888-8888-8888-8888-888888888888",
    @common_id_09 := "99999999-9999-9999-9999-999999999999",
    @common_id_10 := "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa",
    @common_id_11 := "bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb",
    @common_id_12 := "cccccccc-cccc-cccc-cccc-cccccccccccc",
    @common_id_13 := "dddddddd-dddd-dddd-dddd-dddddddddddd",
    @common_id_14 := "eeeeeeee-eeee-eeee-eeee-eeeeeeeeeeee",
    @common_id_15 := "ffffffff-ffff-ffff-ffff-ffffffffffff",
    @datetime := "2022-04-01 00:00:00";

-- affiliates: id, name, postcode, address, tel, fax, email, created_at, updated_at
-- 組織には特権区分つけなくてもいいかも
INSERT INTO affiliates VALUES (@common_id_00, "ツキ寫眞館", "410-0802", "静岡県沼津市上土町36", "090-0300-0300", "090-0300-0300", "tuki@sample.com", @datetime, @datetime);
INSERT INTO affiliates VALUES (@common_id_01, "〇△書店", "410-0804", "静岡県沼津市大手町20", "080-8888-8888", "080-8888-8888", NULL, @datetime, @datetime);
INSERT INTO affiliates VALUES (@common_id_02, "十千万旅館", "410-0842", "静岡県沼津市三津10-5", "055-6767-5858", NULL, "tochiman@sample.com", @datetime, @datetime);
INSERT INTO affiliates VALUES (@common_id_03, "運営", "410-0842", "静岡県沼津市三津10-8", "055-9999-3333", NULL, "mito@sample.com", @datetime, @datetime);

-- users: affiliate_id, id, first_name, last_name, tel, email, created_at, updated_at
-- 一般ユーザ
INSERT INTO users VALUES (@common_id_00, @common_id_00, "月", "渡辺", "090-4649-4649", NULL, @datetime, @datetime);
INSERT INTO users VALUES (@common_id_01, @common_id_01, "花丸", "国木田", "080-8700-8700", NULL, @datetime, @datetime);
INSERT INTO users VALUES (@common_id_02, @common_id_02, "千歌", "高海", "080-7575-7575", "chika@sample.com", @datetime, @datetime);
-- 管理者
INSERT INTO users VALUES (@common_id_03, @common_id_03, "太郎", "Admin", "080-1912-8989", "yamada@sample.com", @datetime, @datetime);

-- items: id, name, description, img_src, category, type, unit_price, sales_start, sales_end, created_at, updated_at
-- 缶バッジ（通常）
INSERT INTO items VALUES (@common_id_00, "ツキ寫眞館 缶バッジ", "ツキ寫眞館絵柄の缶バッジです。", NULL, 0, 0, 300, "2023-04-01 00:00:00", NULL, @datetime, @datetime);
INSERT INTO items VALUES (@common_id_01, "〇△書店 缶バッジ", "〇△書店絵柄の缶バッジです。", NULL, 0, 0, 300, "2023-04-01 00:00:00", NULL, @datetime, @datetime);
INSERT INTO items VALUES (@common_id_02, "十千万旅館 缶バッジ", "十千万旅館絵柄の缶バッジです。", NULL, 0, 0, 300, "2023-04-01 00:00:00", NULL, @datetime, @datetime);
-- 缶バッジ（限定）
INSERT INTO items VALUES (@common_id_03, "クリスマス 缶バッジ 2022", "2022年の限定缶バッジです。", NULL, 0, 1, 300, "2022-12-24 00:00:00", "2023-12-31 11:59:59", @datetime, @datetime);
-- スタンプ帳（通常）
INSERT INTO items VALUES (@common_id_04, "スタンプ帳", "街歩きにつかえるスタンプ帳です。", NULL, 0, 1, 500, "2023-04-01 00:00:00", NULL, @datetime, @datetime);

-- purchase_rights: id, created_at, updated_at, affiliate_id, item_id
INSERT INTO purchase_rights VALUES (@common_id_00, @datetime, @datetime, @common_id_00, @common_id_00);
INSERT INTO purchase_rights VALUES (@common_id_01, @datetime, @datetime, @common_id_01, @common_id_01);
INSERT INTO purchase_rights VALUES (@common_id_02, @datetime, @datetime, @common_id_02, @common_id_02);
-- TODO: 限定アイテム系は誰でもかえるからフラグでいいかも
INSERT INTO purchase_rights VALUES (@common_id_03, @datetime, @datetime, @common_id_00, @common_id_03);
INSERT INTO purchase_rights VALUES (@common_id_04, @datetime, @datetime, @common_id_01, @common_id_03);
INSERT INTO purchase_rights VALUES (@common_id_05, @datetime, @datetime, @common_id_02, @common_id_03);
INSERT INTO purchase_rights VALUES (@common_id_06, @datetime, @datetime, @common_id_00, @common_id_04);
INSERT INTO purchase_rights VALUES (@common_id_07, @datetime, @datetime, @common_id_01, @common_id_04);
INSERT INTO purchase_rights VALUES (@common_id_08, @datetime, @datetime, @common_id_02, @common_id_04);
-- TODO: 管理者も追加の度に権限増えそうだからフラグで管理でよさそう
INSERT INTO purchase_rights VALUES (@common_id_09, @datetime, @datetime, @common_id_03, @common_id_00);
INSERT INTO purchase_rights VALUES (@common_id_10, @datetime, @datetime, @common_id_03, @common_id_01);
INSERT INTO purchase_rights VALUES (@common_id_11, @datetime, @datetime, @common_id_03, @common_id_02);
INSERT INTO purchase_rights VALUES (@common_id_12, @datetime, @datetime, @common_id_03, @common_id_03);
INSERT INTO purchase_rights VALUES (@common_id_13, @datetime, @datetime, @common_id_03, @common_id_04);

-- orders: affiliate_id, user_id, id, postcode, address, approved_flag, created_at, updated_at
-- TODO: 発注者だけじゃなく請求先も必要では
-- 一般購入
INSERT INTO orders VALUES (@common_id_00, @common_id_00, @common_id_00, "410-0802", "静岡県沼津市上土町36", 1, @datetime, @datetime);
INSERT INTO orders VALUES (@common_id_00, @common_id_00, @common_id_01, "410-0802", "静岡県沼津市上土町36", 0, @datetime, @datetime);
-- 管理者購入
INSERT INTO orders VALUES (@common_id_03, @common_id_00, @common_id_02, "410-0842", "静岡県沼津市三津10-5", 1, @datetime, @datetime);
-- 管理者購入（代理）
INSERT INTO orders VALUES (@common_id_03, @common_id_01, @common_id_03, "410-0804", "静岡県沼津市大手町20", 1, @datetime, @datetime);

-- order_items: order_id, item_id, id, quantity, created_at, updated_at
-- 一般購入
INSERT INTO order_items VALUES (@common_id_00, @common_id_00, @common_id_00, 50, @datetime, @datetime);
INSERT INTO order_items VALUES (@common_id_00, @common_id_04, @common_id_01, 30, @datetime, @datetime);
INSERT INTO order_items VALUES (@common_id_01, @common_id_00, @common_id_02, 20, @datetime, @datetime);
INSERT INTO order_items VALUES (@common_id_01, @common_id_03, @common_id_03, 20, @datetime, @datetime);
INSERT INTO order_items VALUES (@common_id_01, @common_id_04, @common_id_04, 20, @datetime, @datetime);
-- 管理者購入
INSERT INTO order_items VALUES (@common_id_02, @common_id_03, @common_id_05, 200, @datetime, @datetime);
INSERT INTO order_items VALUES (@common_id_02, @common_id_04, @common_id_06, 100, @datetime, @datetime);
-- 管理者購入（代理）
INSERT INTO order_items VALUES (@common_id_03, @common_id_01, @common_id_07, 50, @datetime, @datetime);
INSERT INTO order_items VALUES (@common_id_03, @common_id_04, @common_id_08, 20, @datetime, @datetime);
