SELECT AUTHORITY_MEMBER.MEMBER_SEQ, AUTHORITY_MEMBER.AUTHORITY_ID, MEMBER.MEMBER_ID, AUTHORITY.NAME
FROM AUTHORITY INNER JOIN AUTHORITY_MEMBER
    ON AUTHORITY.AUTHORITY_ID = AUTHORITY_MEMBER.AUTHORITY_ID
        INNER JOIN MEMBER
            ON MEMBER.MEMBER_SEQ = AUTHORITY_MEMBER.MEMBER_SEQ AND AUTHORITY.AUTHORITY_ID = 'ROLE_STUDENT';
