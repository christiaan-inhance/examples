// This file was generated by a tool; you should avoid making direct changes.
// Consider using 'partial classes' to extend these types
// Input: cvrptw-acyas3nzweqb.proto

#pragma warning disable CS1591, CS0612, CS3021, IDE1006
namespace Cvrptw
{

    [global::ProtoBuf.ProtoContract()]
    public partial class Geocode : global::ProtoBuf.IExtensible
    {
        private global::ProtoBuf.IExtension __pbn__extensionData;
        global::ProtoBuf.IExtension global::ProtoBuf.IExtensible.GetExtensionObject(bool createIfMissing)
            => global::ProtoBuf.Extensible.GetExtensionObject(ref __pbn__extensionData, createIfMissing);

        [global::ProtoBuf.ProtoMember(1, Name = @"id", IsRequired = true)]
        public string Id { get; set; }

        [global::ProtoBuf.ProtoMember(2, Name = @"x", IsRequired = true)]
        public float X { get; set; }

        [global::ProtoBuf.ProtoMember(3, Name = @"y", IsRequired = true)]
        public float Y { get; set; }

        [global::ProtoBuf.ProtoMember(4, Name = @"quantity", IsRequired = true)]
        public float Quantity { get; set; }

        [global::ProtoBuf.ProtoMember(5)]
        public float windowStart
        {
            get { return __pbn__windowStart.GetValueOrDefault(); }
            set { __pbn__windowStart = value; }
        }
        public bool ShouldSerializewindowStart() => __pbn__windowStart != null;
        public void ResetwindowStart() => __pbn__windowStart = null;
        private float? __pbn__windowStart;

        [global::ProtoBuf.ProtoMember(6)]
        public float windowEnd
        {
            get { return __pbn__windowEnd.GetValueOrDefault(); }
            set { __pbn__windowEnd = value; }
        }
        public bool ShouldSerializewindowEnd() => __pbn__windowEnd != null;
        public void ResetwindowEnd() => __pbn__windowEnd = null;
        private float? __pbn__windowEnd;

    }

    [global::ProtoBuf.ProtoContract(Name = @"CVRPTW")]
    public partial class Cvrptw : global::ProtoBuf.IExtensible
    {
        private global::ProtoBuf.IExtension __pbn__extensionData;
        global::ProtoBuf.IExtension global::ProtoBuf.IExtensible.GetExtensionObject(bool createIfMissing)
            => global::ProtoBuf.Extensible.GetExtensionObject(ref __pbn__extensionData, createIfMissing);

        [global::ProtoBuf.ProtoMember(1, Name = @"points")]
        public global::System.Collections.Generic.List<Geocode> Points { get; } = new global::System.Collections.Generic.List<Geocode>();

        [global::ProtoBuf.ProtoMember(2, Name = @"depot", IsRequired = true)]
        public Geocode Depot { get; set; }

        [global::ProtoBuf.ProtoMember(3, IsRequired = true)]
        public int NumberOfVehicles { get; set; }

        [global::ProtoBuf.ProtoMember(4, IsRequired = true)]
        public float VehicleCapacity { get; set; }

        [global::ProtoBuf.ProtoMember(5, Name = @"distancetype")]
        [global::System.ComponentModel.DefaultValue(eDistanceType.RoadNetwork)]
        public eDistanceType Distancetype
        {
            get { return __pbn__Distancetype ?? eDistanceType.RoadNetwork; }
            set { __pbn__Distancetype = value; }
        }
        public bool ShouldSerializeDistancetype() => __pbn__Distancetype != null;
        public void ResetDistancetype() => __pbn__Distancetype = null;
        private eDistanceType? __pbn__Distancetype;

        [global::ProtoBuf.ProtoContract()]
        public enum eDistanceType
        {
            RoadNetwork = 1,
            Euclidean = 2,
            Haversine = 3,
        }

    }

    [global::ProtoBuf.ProtoContract()]
    public partial class SolveRequest : global::ProtoBuf.IExtensible
    {
        private global::ProtoBuf.IExtension __pbn__extensionData;
        global::ProtoBuf.IExtension global::ProtoBuf.IExtensible.GetExtensionObject(bool createIfMissing)
            => global::ProtoBuf.Extensible.GetExtensionObject(ref __pbn__extensionData, createIfMissing);

        [global::ProtoBuf.ProtoMember(1, Name = @"model")]
        public Cvrptw Model { get; set; }

        [global::ProtoBuf.ProtoMember(2)]
        [global::System.ComponentModel.DefaultValue("")]
        public string modelID
        {
            get { return __pbn__modelID ?? ""; }
            set { __pbn__modelID = value; }
        }
        public bool ShouldSerializemodelID() => __pbn__modelID != null;
        public void ResetmodelID() => __pbn__modelID = null;
        private string __pbn__modelID;

        [global::ProtoBuf.ProtoMember(3, Name = @"visitSequence")]
        public global::System.Collections.Generic.List<string> visitSequences { get; } = new global::System.Collections.Generic.List<string>();

        [global::ProtoBuf.ProtoMember(4)]
        [global::System.ComponentModel.DefaultValue(SolveType.Optimise)]
        public SolveType solveType
        {
            get { return __pbn__solveType ?? SolveType.Optimise; }
            set { __pbn__solveType = value; }
        }
        public bool ShouldSerializesolveType() => __pbn__solveType != null;
        public void ResetsolveType() => __pbn__solveType = null;
        private SolveType? __pbn__solveType;

        [global::ProtoBuf.ProtoContract()]
        public enum SolveType
        {
            Optimise = 0,
            Evaluate = 1,
            ReOptimise = 2,
        }

    }

    [global::ProtoBuf.ProtoContract()]
    public partial class Edge : global::ProtoBuf.IExtensible
    {
        private global::ProtoBuf.IExtension __pbn__extensionData;
        global::ProtoBuf.IExtension global::ProtoBuf.IExtensible.GetExtensionObject(bool createIfMissing)
            => global::ProtoBuf.Extensible.GetExtensionObject(ref __pbn__extensionData, createIfMissing);

        [global::ProtoBuf.ProtoMember(1, Name = @"from", IsRequired = true)]
        public string From { get; set; }

        [global::ProtoBuf.ProtoMember(2, Name = @"to", IsRequired = true)]
        public string To { get; set; }

        [global::ProtoBuf.ProtoMember(3, Name = @"distance")]
        public float Distance
        {
            get { return __pbn__Distance.GetValueOrDefault(); }
            set { __pbn__Distance = value; }
        }
        public bool ShouldSerializeDistance() => __pbn__Distance != null;
        public void ResetDistance() => __pbn__Distance = null;
        private float? __pbn__Distance;

        [global::ProtoBuf.ProtoMember(5, Name = @"geometry")]
        public global::System.Collections.Generic.List<Geometry> Geometries { get; } = new global::System.Collections.Generic.List<Geometry>();

        [global::ProtoBuf.ProtoContract()]
        public partial class Geometry : global::ProtoBuf.IExtensible
        {
            private global::ProtoBuf.IExtension __pbn__extensionData;
            global::ProtoBuf.IExtension global::ProtoBuf.IExtensible.GetExtensionObject(bool createIfMissing)
                => global::ProtoBuf.Extensible.GetExtensionObject(ref __pbn__extensionData, createIfMissing);

            [global::ProtoBuf.ProtoMember(1, Name = @"x", IsRequired = true)]
            public float X { get; set; }

            [global::ProtoBuf.ProtoMember(2, Name = @"y", IsRequired = true)]
            public float Y { get; set; }

        }

    }

    [global::ProtoBuf.ProtoContract()]
    public partial class SolutionResponse : global::ProtoBuf.IExtensible
    {
        private global::ProtoBuf.IExtension __pbn__extensionData;
        global::ProtoBuf.IExtension global::ProtoBuf.IExtensible.GetExtensionObject(bool createIfMissing)
            => global::ProtoBuf.Extensible.GetExtensionObject(ref __pbn__extensionData, createIfMissing);

        [global::ProtoBuf.ProtoMember(1, Name = @"routes")]
        public global::System.Collections.Generic.List<Route> Routes { get; } = new global::System.Collections.Generic.List<Route>();

        [global::ProtoBuf.ProtoMember(2, Name = @"objective", IsRequired = true)]
        public float Objective { get; set; }

        [global::ProtoBuf.ProtoContract()]
        public partial class Route : global::ProtoBuf.IExtensible
        {
            private global::ProtoBuf.IExtension __pbn__extensionData;
            global::ProtoBuf.IExtension global::ProtoBuf.IExtensible.GetExtensionObject(bool createIfMissing)
                => global::ProtoBuf.Extensible.GetExtensionObject(ref __pbn__extensionData, createIfMissing);

            [global::ProtoBuf.ProtoMember(1, Name = @"sequence")]
            public global::System.Collections.Generic.List<string> Sequences { get; } = new global::System.Collections.Generic.List<string>();

            [global::ProtoBuf.ProtoMember(2, Name = @"edges")]
            public global::System.Collections.Generic.List<Edge> Edges { get; } = new global::System.Collections.Generic.List<Edge>();

            [global::ProtoBuf.ProtoMember(3)]
            public float[] visitDistances { get; set; }

        }

    }

}

#pragma warning restore CS1591, CS0612, CS3021, IDE1006
