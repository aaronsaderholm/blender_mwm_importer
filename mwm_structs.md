This is taken from the Space Engineers source code published by Keen: https://github.com/KeenSoftwareHouse/SpaceEngineers
  


```
TAG_TEXCOORDS0  <HalfVector2[] >
TAG_TEXCOORDS1  <HalfVector2[] >
TAG_VERTICES	<HalfVector4[]>
TAG_NORMALS	<Byte4[]>
TAG_BINORMALS <Byte4[] >
TAG_TANGENTS  <Byte4[] >
TAG_RESCALE_FACTOR  <float>(x => x.ReadSingle()) },
TAG_DUMMIES <Dictionary<string, MyModelDummy>>(ReadDummies) },
TAG_BLENDINDICES  <Vector4I[]>(ReadArrayOfVector4Int) },
TAG_BLENDWEIGHTS <Vector4[]>(ReadArrayOfVector4) },
TAG_BONE_MAPPING <Vector3I[]>(ReadArrayOfVector3Int) },

TAG_USE_CHANNEL_TEXTURES	<bool>(x => x.ReadBoolean()) },
TAG_BOUNDING_BOX	<BoundingBox>(ReadBoundingBox) },
TAG_BOUNDING_SPHERE	<BoundingSphere>(ReadBoundingSphere) },

TAG_SWAP_WINDING_ORDER	<bool>(x => x.ReadBoolean()) },

TAG_MESH_PARTS	<List<MyMeshPartInfo>>(ReadMeshParts) },
TAG_MESH_SECTIONS	<List<MyMeshSectionInfo>>(ReadMeshSections) },

 
 TAG_ANIMATIONS	<ModelAnimations>(ReadAnimations) },
 TAG_BONES	<MyModelBone[]>(ReadBones) },
 
 TAG_HAVOK_COLLISION_GEOMETRY	<byte[]>(ReadArrayOfBytes) },
 TAG_PATTERN_SCALE	<float>(x => x.ReadSingle()) },
 TAG_LODS	<MyLODDescriptor[]>(ReadLODs) },
 TAG_HAVOK_DESTRUCTION_GEOMETRY	<byte[]>(ReadArrayOfBytes) },
 TAG_HAVOK_DESTRUCTION	<byte[]>(ReadArrayOfBytes) },
 TAG_FBXHASHSTRING	<VRage.Security.Md5.Hash>(ReadHash) },
 TAG_HKTHASHSTRING	<VRage.Security.Md5.Hash>(ReadHash) },
 TAG_XMLHASHSTRING	<VRage.Security.Md5.Hash>(ReadHash) },
 TAG_MODEL_FRACTURES	<MyModelFractures>(ReadModelFractures) },


 TAG_MODEL_BVH  <GImpactQuantizedBvh>(delegate(BinaryReader reader) 
               {
                   GImpactQuantizedBvh bvh = new GImpactQuantizedBvh(); 
                   bvh.Load(ReadArrayOfBytes(reader)); 
                   return bvh; 
               }  ) },
TAG_MODEL_INFO  <MyModelInfo>(delegate(BinaryReader reader)
               {
                    int tri, vert;
                    Vector3 bb;
                    tri = reader.ReadInt32();
                    vert = reader.ReadInt32();
                    bb = ImportVector3(reader);
                    return new MyModelInfo(tri, vert, bb);
            } ) },
```