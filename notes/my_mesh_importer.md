```
public bool Import(BinaryReader reader, int version)
{
    m_MaterialHash = reader.ReadInt32();
    if (version < 01052001)
        reader.ReadInt32(); //MyMeshDrawTechnique

    int nCount = reader.ReadInt32();
    for (int i = 0; i < nCount; ++i)
    {
        m_indices.Add(reader.ReadInt32());
    }

    bool bMatDesc = reader.ReadBoolean();
    bool bRes = true;
    if (bMatDesc)
    {
        m_MaterialDesc = new MyMaterialDescriptor();
        bRes = m_MaterialDesc.Read(reader, version);

        bRes &= Enum.TryParse(m_MaterialDesc.Technique, out Technique);
    }
    else
    {
        m_MaterialDesc = null;
    }

    return bRes;
}
```